from tap_amazon_advertising.streams.base import PaginatedStream

import singer
import json

LOGGER = singer.get_logger()  # noqa


class BiddableKeywordsStream(PaginatedStream):
    API_METHOD = 'GET'
    TABLE = 'ad_group_biddable_keywords'
    KEY_PROPERTIES = ['keywordId']

    @property
    def api_path(self):
        return '/v2/sp/keywords/extended'

    def get_stream_data(self, result):
        return [
            self.transform_record(record)
            for record in result
        ]
