from tap_amazon_advertising.streams.base import PaginatedStream

import singer
import json

LOGGER = singer.get_logger()  # noqa


class CampaignsStream(PaginatedStream):
    API_METHOD = 'GET'
    TABLE = 'campaigns'
    KEY_PROPERTIES = ['campaignId']

    @property
    def api_path(self):
        return '/v2/campaigns/extended'

    def get_stream_data(self, result):
        return [
            self.transform_record(record)
            for record in result
        ]
