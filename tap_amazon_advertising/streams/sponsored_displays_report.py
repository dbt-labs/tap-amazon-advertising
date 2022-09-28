import singer

from tap_amazon_advertising.streams.base import ReportStream

LOGGER = singer.get_logger()  # noqa


class BaseSponsoredDisplaysReportStream(ReportStream):
    API_METHOD = 'GET'

    @property
    def recordType(self):
        raise RuntimeError("not implemented")

    @property
    def api_path(self):
        return '/sd/{}/report'.format(self.recordType)

    def get_body(self, day):
        raise RuntimeError("Not implemented")

    def get_stream_data(self, result, day):
        for record in result:
            record['day'] = day.isoformat()

        return [
            self.transform_record(record)
            for record in result
        ]


class SponsoredDisplaysReportProductAdsStream(BaseSponsoredDisplaysReportStream):
    TABLE = 'sponsored_displays_report_product_ads'
    KEY_PROPERTIES = ['adId', 'day', 'profileId']

    @property
    def recordType(self):
        return "productAds"

    def get_body(self, day):
        return {
            "tactic": "T00020",
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
                "adId",
                "asin",
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
                "attributedOrdersNewToBrand14d",
                "attributedSalesNewToBrand14d",
                "attributedUnitsOrderedNewToBrand14d",
                "attributedDetailPageView14d",
                "viewImpressions",
                "viewAttributedConversions14d",
                "viewAttributedSales14d",
                "viewAttributedUnitsOrdered14d",
                "viewAttributedDetailPageView14d",
            ])
        }


class SponsoredDisplaysReportProductAdsAudiencesStream(SponsoredDisplaysReportProductAdsStream):
    TABLE = 'sponsored_displays_report_product_ads_audiences'

    def get_body(self, day):
        body = super().get_body(day)
        body["tactic"] = "T00030"
        return body


class SponsoredDisplaysReportAdGroupsStream(BaseSponsoredDisplaysReportStream):
    TABLE = 'sponsored_displays_report_ad_groups'
    KEY_PROPERTIES = ['adGroupId', 'day', 'profileId']

    @property
    def recordType(self):
        return "adGroups"

    def get_body(self, day):
        return {
            "tactic": "T00020",
            "reportDate": day.strftime('%Y%m%d'),
            "metrics": ",".join([
                "campaignName",
                "campaignId",
                "bidOptimization",
                "adGroupName",
                "adGroupId",
                "impressions",
                "clicks",
                "cost",
                "currency",
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
                "attributedOrdersNewToBrand14d",
                "attributedSalesNewToBrand14d",
                "attributedUnitsOrderedNewToBrand14d",
                "attributedDetailPageView14d",
                "viewImpressions",
                "viewAttributedConversions14d",
                "viewAttributedSales14d",
                "viewAttributedUnitsOrdered14d",
                "attributedDetailPageView14d",
                "viewAttributedDetailPageView14d",
            ])
        }


class SponsoredDisplaysReportAdGroupsAudiencesStream(SponsoredDisplaysReportAdGroupsStream):
    TABLE = 'sponsored_displays_report_ad_groups_audiences'

    def get_body(self, day):
        body = super().get_body(day)
        body["tactic"] = "T00030"
        return body


class SponsoredDisplaysReportCampaignsStream(BaseSponsoredDisplaysReportStream):
    TABLE = 'sponsored_displays_report_campaigns'
    KEY_PROPERTIES = ['campaignId', 'day', 'profileId']

    def get_body(self, day):
        return {
            "tactic": "T00020",
            "reportDate": day.strftime('%Y%m%d'),
            "metrics": ",".join([
                "campaignName",
                "campaignId",
                "costType",
                "impressions",
                "clicks",
                "cost",
                "currency",
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
                "attributedOrdersNewToBrand14d",
                "attributedSalesNewToBrand14d",
                "attributedUnitsOrderedNewToBrand14d",
                "viewImpressions",
                "viewAttributedConversions14d",
                "viewAttributedSales14d",
                "viewAttributedUnitsOrdered14d",
                "attributedDetailPageView14d",
                "viewAttributedDetailPageView14d",
            ])
        }

    @property
    def recordType(self):
        return "campaigns"


class SponsoredDisplaysReportCampaignsAudiencesStream(SponsoredDisplaysReportCampaignsStream):
    TABLE = 'sponsored_displays_report_campaigns_audiences'

    def get_body(self, day):
        body = super().get_body(day)
        body["tactic"] = "T00030"
        return body


class SponsoredDisplaysReportTargetsStream(BaseSponsoredDisplaysReportStream):
    TABLE = 'sponsored_displays_report_targets'
    KEY_PROPERTIES = ['targetId', 'day', 'profileId']

    def get_body(self, day):
        return {
            "tactic": "T00020",
            "reportDate": day.strftime('%Y%m%d'),
            "metrics": ",".join(
                ['adGroupId', 'adGroupName', 'attributedConversions14d', 'attributedConversions14dSameSKU',
                 'attributedConversions1d', 'attributedConversions1dSameSKU', 'attributedConversions30d',
                 'attributedConversions30dSameSKU', 'attributedConversions7d', 'attributedConversions7dSameSKU',
                 'attributedDetailPageView14d', 'attributedOrdersNewToBrand14d', 'attributedSales14d',
                 'attributedSales14dSameSKU', 'attributedSales1d', 'attributedSales1dSameSKU', 'attributedSales30d',
                 'attributedSales30dSameSKU', 'attributedSales7d', 'attributedSales7dSameSKU',
                 'attributedSalesNewToBrand14d', 'attributedUnitsOrdered14d', 'attributedUnitsOrdered1d',
                 'attributedUnitsOrdered30d', 'attributedUnitsOrdered7d', 'attributedUnitsOrderedNewToBrand14d',
                 'campaignId', 'campaignName', 'clicks', 'cost', 'currency', 'impressions', 'targetId',
                 'targetingExpression', 'targetingText', 'targetingType', 'viewImpressions',
                 'viewAttributedConversions14d', 'viewAttributedDetailPageView14d', 'viewAttributedSales14d',
                 'viewAttributedUnitsOrdered14d', 'viewAttributedOrdersNewToBrand14d',
                 'viewAttributedSalesNewToBrand14d', 'viewAttributedUnitsOrderedNewToBrand14d',
                 'attributedBrandedSearches14d', 'viewAttributedBrandedSearches14d']
                )
        }

    @property
    def recordType(self):
        return "targets"
