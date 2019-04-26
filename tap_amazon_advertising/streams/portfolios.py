from tap_amazon_advertising.streams.base import BaseStream

import singer
import json

LOGGER = singer.get_logger()  # noqa


class PortfoliosStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'portfolios'
    KEY_PROPERTIES = ['portfolioId']

    @property
    def api_path(self):
        return '/v2/portfolios/extended'

    def get_stream_data(self, result):
        return [
            self.transform_record(record)
            for record in result
        ]
