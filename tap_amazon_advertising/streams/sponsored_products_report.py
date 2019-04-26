from tap_amazon_advertising.streams.base import ReportStream

import singer
import json

LOGGER = singer.get_logger()  # noqa

class BaseSponsoredProductsReportStream(ReportStream):
    API_METHOD = 'GET'

    @property
    def recordType(self):
        raise RuntimeError("not implemented")

    @property
    def api_path(self):
        return '/v2/sp/{}/report'.format(self.recordType)

    def get_body(self, day):
        return {
            "reportDate": day.strftime('%Y%m%d'),
            "metrics": ",".join([
                "campaignName",
                "campaignId",
                "adGroupName",
                "adGroupId",
                "impressions",
                "clicks",
                "cost",
                "currency",
                "asin",
                "sku",
                "attributedConversions1d",
                "attributedConversions7d",
                "attributedConversions14d",
                "attributedConversions30d",
                "attributedConversions1dSameSKU",
                "attributedConversions7dSameSKU",
                "attributedConversions14dSameSKU",
                "attributedConversions30dSameSKU",
                "attributedUnitsOrdered1d",
                "attributedUnitsOrdered7d",
                "attributedUnitsOrdered14d",
                "attributedUnitsOrdered30d",
                "attributedSales1d",
                "attributedSales7d",
                "attributedSales14d",
                "attributedSales30d",
                "attributedSales1dSameSKU",
                "attributedSales7dSameSKU",
                "attributedSales14dSameSKU",
                "attributedSales30dSameSKU",
            ])
        }

    def get_stream_data(self, result, day):
        for record in result:
            record['day'] = day.isoformat()

        return [
            self.transform_record(record)
            for record in result
        ]


class SponsoredProductsReportProductAdsStream(BaseSponsoredProductsReportStream):
    TABLE = 'sponsored_products_report_product_ads'
    KEY_PROPERTIES = ['adId', 'day']

    @property
    def recordType(self):
        return "productAds"
