from tap_amazon_advertising.streams.base import PaginatedStream

import singer
import json

LOGGER = singer.get_logger()  # noqa


class SponsoredProductsCampaignsStream(PaginatedStream):
    API_METHOD = 'GET'
    TABLE = 'sponsored_products_campaigns'
    KEY_PROPERTIES = ['campaignId', 'profileId']

    @property
    def api_path(self):
        return '/v2/sp/campaigns/extended'

    def get_stream_data(self, result):
        return [
            self.transform_record(record)
            for record in result
        ]
