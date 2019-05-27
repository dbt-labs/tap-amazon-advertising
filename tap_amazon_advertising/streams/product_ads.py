from tap_amazon_advertising.streams.base import PaginatedStream

import singer
import json

LOGGER = singer.get_logger()  # noqa


class ProductAdsStream(PaginatedStream):
    API_METHOD = 'GET'
    TABLE = 'product_ads'
    KEY_PROPERTIES = ['profileId', 'adId']

    @property
    def api_path(self):
        return '/v2/sp/productAds/extended'

    def get_stream_data(self, result):
        return [
            self.transform_record(record)
            for record in result
        ]
