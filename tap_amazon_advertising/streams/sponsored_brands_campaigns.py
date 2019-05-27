from tap_amazon_advertising.streams.base import PaginatedStream

import singer
import json

LOGGER = singer.get_logger()  # noqa


class SponsoredBrandsCampaignsStream(PaginatedStream):
    API_METHOD = 'GET'
    TABLE = 'sponsored_brands_campaigns'
    KEY_PROPERTIES = ['profileId', 'campaignId']

    @property
    def api_path(self):
        return '/v2/hsa/campaigns'

    def get_stream_data(self, result):
        return [
            self.transform_record(record)
            for record in result
        ]
