import requests
import requests_oauthlib
import singer
import singer.metrics

import zlib
import json
import time

LOGGER = singer.get_logger()  # noqa

TOKEN_URL = 'https://api.amazon.com/auth/o2/token'
SCOPES = ["advertising:campaign_management"]


class AmazonAdvertisingClient:

    MAX_TRIES = 5

    def __init__(self, config):
        self.config = config
        self.access_token = self.get_authorization()
        self.profile_id = None

    def set_profile_id(self, profile_id):
        self.profile_id = profile_id

    def get_authorization(self):
        #return 'Atza|IwEBIGscxiYf1OO9l4mRQEY1UPOH5fnRUroEQwRBmCSS7GP9rs2a90KsQDz1DVJIKtXhvdBottH1eybpnW6UgLXK8A7WVk2gXzNlXRUmHCJ8Py36m2Qbtcw3kYzjmrr89AUdspeZAtiFEtU9CyHZKBZ-YFZCIPfxj1BhdElyqy_2iIzL-mUKqAZPlM1WWH93hpkSLkzNGKPbN3WZR9h3jjJgqjHumWGtOA_7qEyJLmAbJ8jH0taQEArGWvNfL-b3rcSDDwn0kMUaeZRKJgxURghGjdv6vXNy-N-imYcHoZv5vs1aGkOC4ETZP2J7VJpphSPDhMmGjOQL72xJv0-UOpHVoLvadqPjlYhLLf6Vgja1p873ovrk01LTc8kU7w-fkHunusfkL7AjoNTGL9-s9jhDTwrItL56hNYR-6RJ7D5B3UqZ0NSH0a58SknYveEJTi21p_i_frvonPUxZ3HUUdosoLm-pR43XE97z9BUynrFBMQmyA'
        client_id = self.config.get('client_id')
        oauth = requests_oauthlib.OAuth2Session(
                    client_id,
                    redirect_uri=self.config.get('redirect_uri'),
                    scope=SCOPES)

        tokens = oauth.refresh_token(
                    TOKEN_URL,
                    refresh_token=self.config.get('refresh_token'),
                    client_id=self.config.get('client_id'),
                    client_secret=self.config.get('client_secret'))

        return tokens['access_token']

    def _make_request(self, url, method, params=None, body=None, attempts=0):
        if not self.profile_id:
            raise RuntimeError("Client profile_id is None!")

        LOGGER.info("Making {} request to {} ({})".format(method, url, params))

        kwargs = {
            'headers': {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(self.access_token),
                'Amazon-Advertising-API-ClientId': self.config.get('client_id'),
                'Amazon-Advertising-API-Scope': self.profile_id,
            },
            'params': params,
        }
        if body:
            kwargs['json'] = body

        response = requests.request(
            method,
            url,
            **kwargs)

        LOGGER.info("Received code: {}".format(response.status_code))

        if attempts < self.MAX_TRIES and response.status_code in [429, 502, 401]:
            if response.status_code == 401:
                LOGGER.info("Received unauthorized error code, retrying: {}".format(response.text))
                self.access_token = self.get_authorization()

            else:
                LOGGER.info("Received rate limit response, sleeping: {}".format(response.text))
                time.sleep(30)

            return self._make_request(url, method, params, body, attempts+1)

        if response.status_code not in [200, 201, 202]:
            raise RuntimeError(response.text)

        return response

    def make_request(self, url, method, params=None, body=None):
        return self._make_request(url, method, params, body).json()

    def download_gzip(self, url):
        resp = None
        attempts = 3
        for i in range(attempts + 1):
            try:
                resp = self._make_request(url, 'GET')
                break
            except ConnectionError as e:
                LOGGER.info("Caught error while downloading gzip, sleeping: {}".format(e))
                time.sleep(10)
        else:
            raise RuntimeError("Unable to sync gzip after {} attempts".format(attempts))

        return self.unzip(resp.content)

    @classmethod
    def unzip(cls, blob):
        extracted = zlib.decompress(blob, 16+zlib.MAX_WBITS)
        decoded = extracted.decode('utf-8')
        return json.loads(decoded)
