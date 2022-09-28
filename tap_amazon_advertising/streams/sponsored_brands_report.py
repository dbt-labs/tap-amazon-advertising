import singer

from tap_amazon_advertising.streams.base import ReportStream

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
        raise RuntimeError("Not implemented")

    def get_stream_data(self, result, day):
        for record in result:
            record['day'] = day.isoformat()

        return [
            self.transform_record(record)
            for record in result
        ]


class SponsoredBrandsReportKeywordsStream(BaseSponsoredBrandsReportStream):
    TABLE = 'sponsored_brands_report_keywords'
    KEY_PROPERTIES = ['keywordId', 'day', 'profileId']

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

    @property
    def recordType(self):
        return "keywords"


class SponsoredBrandsVideoReportKeywordsStream(BaseSponsoredBrandsReportStream):
    TABLE = "sponsored_brands_video_report_keywords"
    KEY_PROPERTIES = ['keywordId', 'day', 'profileId']

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
                "viewableImpressions",
                "videoFirstQuartileViews",
                "videoMidpointViews",
                "videoThirdQuartileViews",
                "videoCompleteViews",
                "video5SecondViews",
                "video5SecondViewRate",
                "videoUnmutes",
                "vtr",
                "vctr",
            ]),
            "creativeType": "video"
        }

    @property
    def recordType(self):
        return "keywords"


class SponsoredBrandsReportAdGroupsStream(BaseSponsoredBrandsReportStream):
    TABLE = 'sponsored_brands_report_ad_groups'
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
                "campaignStatus",
                "campaignBudget",
                "campaignBudgetType",
                "adGroupName",
                "adGroupId",
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


class SponsoredBrandsVideoReportAdGroupsStream(BaseSponsoredBrandsReportStream):
    TABLE = "sponsored_brands_video_report_ad_groups"
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
                "campaignStatus",
                "campaignBudget",
                "campaignBudgetType",
                "adGroupName",
                "adGroupId",
                "impressions",
                "clicks",
                "cost",
                "attributedSales14d",
                "attributedSales14dSameSKU",
                "attributedConversions14d",
                "attributedConversions14dSameSKU",
                "viewableImpressions",
                "videoFirstQuartileViews",
                "videoMidpointViews",
                "videoThirdQuartileViews",
                "videoCompleteViews",
                "video5SecondViews",
                "video5SecondViewRate",
                "videoUnmutes",
                "vtr",
                "vctr",
            ]),
            "creativeType": "video"
        }


class SponsoredBrandsReportCampaignsStream(BaseSponsoredBrandsReportStream):
    TABLE = 'sponsored_brands_report_campaigns'
    KEY_PROPERTIES = ['campaignId', 'day', 'profileId']

    def get_body(self, day):
        return {
            "reportDate": day.strftime('%Y%m%d'),
            "metrics": ",".join([
                "campaignName",
                "campaignId",
                "campaignStatus",
                "campaignBudget",
                "campaignBudgetType",
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

    @property
    def recordType(self):
        return "campaigns"


class SponsoredBrandsVideoReportCampaignsStream(BaseSponsoredBrandsReportStream):
    TABLE = "sponsored_brands_video_report_campaigns"
    KEY_PROPERTIES = ['campaignId', 'day', 'profileId']

    @property
    def recordType(self):
        return "campaigns"

    def get_body(self, day):
        return {
            "reportDate": day.strftime('%Y%m%d'),
            "metrics": ",".join([
                "campaignName",
                "campaignId",
                "campaignStatus",
                "campaignBudget",
                "campaignBudgetType",
                "impressions",
                "clicks",
                "cost",
                "attributedSales14d",
                "attributedSales14dSameSKU",
                "attributedConversions14d",
                "attributedConversions14dSameSKU",
                "viewableImpressions",
                "videoFirstQuartileViews",
                "videoMidpointViews",
                "videoThirdQuartileViews",
                "videoCompleteViews",
                "video5SecondViews",
                "video5SecondViewRate",
                "videoUnmutes",
                "vtr",
                "vctr",
            ]),
            "creativeType": "video"
        }


class SponsoredBrandsReportSearchTermsStream(SponsoredBrandsReportKeywordsStream):
    TABLE = 'sponsored_brands_report_search_terms'

    def get_body(self, day):
        body = super().get_body(day)
        body["segment"] = "query"
        body["metrics"] = ",".join(
            ['adGroupId', 'adGroupName', 'attributedConversions14d', 'attributedSales14d', 'campaignBudget',
             'campaignBudgetType', 'campaignId', 'campaignName', 'campaignStatus', 'clicks', 'cost', 'impressions',
             'keywordBid', 'keywordId', 'keywordStatus', 'keywordText', 'matchType',
             'searchTermImpressionRank', 'searchTermImpressionShare']
        )
        return body


class SponsoredBrandsVideoReportSearchTermsStream(SponsoredBrandsVideoReportKeywordsStream):
    TABLE = 'sponsored_brands_video_report_search_terms'

    def get_body(self, day):
        body = super().get_body(day)
        body["segment"] = "query"
        body["metrics"] = ",".join(
            ['adGroupId', 'adGroupName', 'attributedConversions14d', 'attributedSales14d', 'campaignBudget',
             'campaignBudgetType', 'campaignStatus', 'clicks', 'cost', 'impressions', 'keywordBid', 'keywordId',
             'keywordStatus', 'keywordText', 'matchType', 'vctr', 'video5SecondViewRate', 'video5SecondViews',
             'videoCompleteViews', 'videoFirstQuartileViews', 'videoMidpointViews', 'videoThirdQuartileViews',
             'videoUnmutes', 'viewableImpressions', 'vtr']
        )
        return body


class SponsoredBrandsReportTargets(BaseSponsoredBrandsReportStream):
    TABLE = "sponsored_brands_report_targets"
    KEY_PROPERTIES = ['targetId', 'day', 'profileId']

    @property
    def recordType(self):
        return "targets"

    def get_body(self, day):
        return {
            "reportDate": day.strftime('%Y%m%d'),
            "metrics": ",".join(
                ['adGroupId', 'adGroupName', 'attributedConversions14d', 'attributedConversions14dSameSKU',
                 'attributedDetailPageViewsClicks14d', 'attributedOrderRateNewToBrand14d',
                 'attributedOrdersNewToBrand14d', 'attributedOrdersNewToBrandPercentage14d', 'attributedSales14d',
                 'attributedSales14dSameSKU', 'attributedSalesNewToBrand14d', 'attributedSalesNewToBrandPercentage14d',
                 'attributedUnitsOrderedNewToBrand14d', 'attributedUnitsOrderedNewToBrandPercentage14d',
                 'campaignBudget', 'campaignBudgetType', 'campaignId', 'campaignName', 'campaignStatus', 'clicks',
                 'cost', 'dpv14d', 'impressions', 'targetId', 'targetingExpression', 'targetingText', 'targetingType',
                 'unitsSold14d', 'attributedBrandedSearches14d']

            )
        }


class SponsoredBrandsVideoReportTargets(BaseSponsoredBrandsReportStream):
    TABLE = "sponsored_brands_video_report_targets"
    KEY_PROPERTIES = ['targetId', 'day', 'profileId']

    @property
    def recordType(self):
        return "targets"

    def get_body(self, day):
        return {
            "reportDate": day.strftime('%Y%m%d'),
            "metrics": ",".join(
                ['adGroupId', 'adGroupName', 'attributedConversions14d', 'attributedConversions14dSameSKU',
                 'attributedSales14d', 'attributedSales14dSameSKU', 'campaignBudget', 'campaignBudgetType',
                 'campaignId', 'campaignName', 'campaignStatus', 'clicks', 'cost', 'impressions', 'targetId',
                 'targetingExpression', 'targetingText', 'targetingType', 'vctr', 'video5SecondViewRate',
                 'video5SecondViews', 'videoCompleteViews', 'videoFirstQuartileViews', 'videoMidpointViews',
                 'videoThirdQuartileViews', 'videoUnmutes', 'viewableImpressions', 'vtr', 'dpv14d',
                 'attributedDetailPageViewsClicks14d', 'attributedOrderRateNewToBrand14d',
                 'attributedOrdersNewToBrand14d', 'attributedOrdersNewToBrandPercentage14d',
                 'attributedSalesNewToBrand14d', 'attributedSalesNewToBrandPercentage14d',
                 'attributedUnitsOrderedNewToBrand14d', 'attributedUnitsOrderedNewToBrandPercentage14d',
                 'attributedBrandedSearches14d']
            ),
            "creativeType": "all"
        }
