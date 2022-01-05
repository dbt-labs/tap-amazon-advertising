from tap_amazon_advertising.streams.base import PaginatedStream


class SponsoredDisplaysCampaignsStream(PaginatedStream):
    API_METHOD = 'GET'
    TABLE = 'sponsored_displays_campaigns'
    KEY_PROPERTIES = ['profileId', 'campaignId']

    @property
    def api_path(self):
        return '/v2/sd/campaigns/extended'

    def get_stream_data(self, result):
        return [
            self.transform_record(record)
            for record in result
        ]


class SponsoredDisplaysAdGroupsStream(PaginatedStream):
    API_METHOD = 'GET'
    TABLE = 'sponsored_displays_ad_groups'
    KEY_PROPERTIES = ['profileId', 'adGroupId']

    @property
    def api_path(self):
        return '/v2/sd/adGroups/extended'

    def get_stream_data(self, result):
        return [
            self.transform_record(record)
            for record in result
        ]


class SponsoredDisplaysProductAdsStream(PaginatedStream):
    API_METHOD = 'GET'
    TABLE = 'sponsored_displays_product_ads'
    KEY_PROPERTIES = ['adId', 'adGroupId']

    @property
    def api_path(self):
        return '/v2/sd/productAds/extended'

    def get_stream_data(self, result):
        return [
            self.transform_record(record)
            for record in result
        ]
