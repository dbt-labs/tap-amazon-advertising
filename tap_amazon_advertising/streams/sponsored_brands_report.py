from tap_amazon_advertising.streams.base import ReportStream

import singer
import json

LOGGER = singer.get_logger()  # noqa


class BaseSponsoredBrandsReportStream(ReportStream):
    API_METHOD = 'GET'

    @property
    def recordType(self):
        raise RuntimeError("not implemented")

    @property
    def api_path(self):
        return '/v2/hsa/{}/report'.format(self.recordType)

    def get_body(self, day):
        return {
            "reportDate": day.strftime('%Y%m%d'),
            "metrics": ",".join([
                "campaignName",
                "campaignId",
                "campaignStatus",
                "campaignBudget",
                "campaignBudgetType",
                "adGroupName",
                "adGroupId",
                "keywordText",
                "matchType",
                "impressions",
                "clicks",
                "cost",
                "attributedSales14d",
                "attributedSales14dSameSKU",
                "attributedConversions14d",
                "attributedConversions14dSameSKU",
                "attributedOrdersNewToBrand14d",
                "attributedOrdersNewToBrandPercentage14d",
                "attributedOrderRateNewToBrand14d",
                "attributedSalesNewToBrand14d",
                "attributedSalesNewToBrandPercentage14d",
                "attributedUnitsOrderedNewToBrand14d",
                "attributedUnitsOrderedNewToBrandPercentage14d",
            ])
        }

    def get_stream_data(self, result, day):
        for record in result:
            record['day'] = day.isoformat()

        return [
            self.transform_record(record)
            for record in result
        ]

class SponsoredBrandsReportKeywordsStream(BaseSponsoredBrandsReportStream):
    TABLE = 'sponsored_brands_report_keywords'
    KEY_PROPERTIES = ['keywordId', 'day']

    @property
    def recordType(self):
        return "keywords"
