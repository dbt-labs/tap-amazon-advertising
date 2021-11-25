from tap_amazon_advertising.streams.base import PaginatedStream

import singer
import json

LOGGER = singer.get_logger()  # noqa


class SponsoredDisplayCampaignsStream(PaginatedStream):
    API_METHOD = 'GET'
    TABLE = 'sponsored_display_campaigns'
    KEY_PROPERTIES = ['campaignId', 'profileId']

    @property
    def api_path(self):
        return '/sd/campaigns/extended'

    def get_stream_data(self, result):
        return [
            self.transform_record(record)
            for record in result
        ]
