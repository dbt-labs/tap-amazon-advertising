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
    KEY_PROPERTIES = ['adId', 'day', 'profileId']

    @property
    def recordType(self):
        return "productAds"

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
                # "sku", # Not supported for vendors?
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


class SponsoredProductsReportCampaignsStream(BaseSponsoredProductsReportStream):
    TABLE = 'sponsored_products_report_campaigns'
    KEY_PROPERTIES = ['campaignId', 'day', 'profileId']

    @property
    def recordType(self):
        return "campaigns"

    def get_body(self, day):
        return {
            "reportDate": day.strftime('%Y%m%d'),
            "metrics": ",".join([
                "bidPlus",
                "campaignName",
                "campaignId",
                "campaignStatus",
                "campaignBudget",
                "impressions",
                "clicks",
                "cost",
                "portfolioId",
                "portfolioName",
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


class SponsoredProductsReportAdGroupsStream(BaseSponsoredProductsReportStream):
    TABLE = 'sponsored_products_report_ad_groups'
    KEY_PROPERTIES = ['adGroupId', 'day', 'profileId']

    @property
    def recordType(self):
        return "adGroups"

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


class SponsoredProductsReportKeywordsStream(BaseSponsoredProductsReportStream):
    TABLE = 'sponsored_products_report_keywords'
    KEY_PROPERTIES = ['keywordId', 'day', 'profileId']

    @property
    def recordType(self):
        return "keywords"

    def get_body(self, day):
        return {
            "reportDate": day.strftime('%Y%m%d'),
            "metrics": ",".join([
                "campaignName",
                "campaignId",
                "keywordId",
                "keywordText",
                "matchType",
                "impressions",
                "clicks",
                "cost",
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


class SponsoredProductsReportTargetStream(BaseSponsoredProductsReportStream):
    TABLE = 'sponsored_products_report_targets'
    KEY_PROPERTIES = ['targetId', 'day', 'profileId']

    @property
    def recordType(self):
        return "targets"

    def get_body(self, day):
        return {
            "reportDate": day.strftime('%Y%m%d'),
            "metrics": ",".join(
                ['adGroupId', 'adGroupName', 'attributedConversions14d', 'attributedConversions14dSameSKU',
                 'attributedConversions1d', 'attributedConversions1dSameSKU', 'attributedConversions30d',
                 'attributedConversions30dSameSKU', 'attributedConversions7d', 'attributedConversions7dSameSKU',
                 'attributedSales14d', 'attributedSales14dSameSKU', 'attributedSales1d', 'attributedSales1dSameSKU',
                 'attributedSales30d', 'attributedSales30dSameSKU', 'attributedSales7d', 'attributedSales7dSameSKU',
                 'attributedUnitsOrdered14d', 'attributedUnitsOrdered14dSameSKU', 'attributedUnitsOrdered1d',
                 'attributedUnitsOrdered1dSameSKU', 'attributedUnitsOrdered30d', 'attributedUnitsOrdered30dSameSKU',
                 'attributedUnitsOrdered7d', 'attributedUnitsOrdered7dSameSKU', 'campaignBudget', 'campaignBudgetType',
                 'campaignId', 'campaignName', 'campaignStatus', 'clicks', 'cost', 'impressions', 'targetId',
                 'targetingExpression', 'targetingText', 'targetingType']

            )
        }


class SponsoredProductsReportSearchTermsKeywordStream(SponsoredProductsReportKeywordsStream):
    TABLE = 'sponsored_products_report_search_terms_keyword'

    def get_body(self, day):
        body = super().get_body(day)
        body["segment"] = "query"
        return body


class SponsoredProductsReportSearchTermsTargetStream(SponsoredProductsReportTargetStream):
    TABLE = 'sponsored_products_report_search_terms_target'

    def get_body(self, day):
        body = super().get_body(day)
        body["segment"] = "query"
        return body