from tap_amazon_advertising.streams.base import BaseStream

import singer
import json

LOGGER = singer.get_logger()  # noqa


class ProfilesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'profiles'
    KEY_PROPERTIES = ['profileId']

    @property
    def api_path(self):
        return '/v2/profiles'

    def get_stream_data(self, result):
        return [
            self.transform_record(record)
            for record in result
        ]
