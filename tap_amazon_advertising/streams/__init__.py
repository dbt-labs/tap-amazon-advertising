from tap_amazon_advertising.streams.dsp import DSPOrders
from tap_amazon_advertising.streams.profiles import ProfilesStream
from tap_amazon_advertising.streams.portfolios import PortfoliosStream
from tap_amazon_advertising.streams.sponsored_displays import SponsoredDisplaysAdGroupsStream, SponsoredDisplaysCampaignsStream, SponsoredDisplaysProductAdsStream
from tap_amazon_advertising.streams.sponsored_displays_report import SponsoredDisplaysReportAdGroupsStream, \
    SponsoredDisplaysReportCampaignsStream, SponsoredDisplaysReportProductAdsStream, \
    SponsoredDisplaysReportProductAdsAudiencesStream, SponsoredDisplaysReportCampaignsAudiencesStream, \
    SponsoredDisplaysReportAdGroupsAudiencesStream
from tap_amazon_advertising.streams.sponsored_products_campaigns import SponsoredProductsCampaignsStream
from tap_amazon_advertising.streams.sponsored_brands_campaigns import SponsoredBrandsCampaignsStream
from tap_amazon_advertising.streams.ad_groups import AdGroupsStream
from tap_amazon_advertising.streams.biddable_keywords import BiddableKeywordsStream
from tap_amazon_advertising.streams.negative_keywords import NegativeKeywordsStream
from tap_amazon_advertising.streams.campaign_negative_keywords import CampaignNegativeKeywordsStream
from tap_amazon_advertising.streams.product_ads import ProductAdsStream

from tap_amazon_advertising.streams.sponsored_products_report import SponsoredProductsReportProductAdsStream, \
        SponsoredProductsReportCampaignsStream, \
        SponsoredProductsReportAdGroupsStream, \
        SponsoredProductsReportKeywordsStream

from tap_amazon_advertising.streams.sponsored_brands_report import SponsoredBrandsReportKeywordsStream, \
    SponsoredBrandsReportCampaignsStream, \
    SponsoredBrandsReportAdGroupsStream, \
    SponsoredBrandsVideoReportCampaignsStream, \
    SponsoredBrandsVideoReportKeywordsStream, \
    SponsoredBrandsVideoReportAdGroupsStream

AVAILABLE_STREAMS = [
    ProfilesStream,
    PortfoliosStream,
    SponsoredProductsCampaignsStream,
    SponsoredBrandsCampaignsStream,
    AdGroupsStream,
    BiddableKeywordsStream,
    NegativeKeywordsStream,
    CampaignNegativeKeywordsStream,
    ProductAdsStream,

    # SP Reports
    SponsoredProductsReportProductAdsStream,
    SponsoredProductsReportCampaignsStream,
    SponsoredProductsReportAdGroupsStream,
    SponsoredProductsReportKeywordsStream,

    # SB Reports
    SponsoredBrandsReportKeywordsStream,
    SponsoredBrandsReportCampaignsStream,
    SponsoredBrandsReportAdGroupsStream,

    # SB video Reports
    SponsoredBrandsVideoReportKeywordsStream,
    SponsoredBrandsVideoReportCampaignsStream,
    SponsoredBrandsVideoReportAdGroupsStream,

    # SD Streams
    SponsoredDisplaysAdGroupsStream,
    SponsoredDisplaysCampaignsStream,
    SponsoredDisplaysProductAdsStream,

    # SD Reports
    SponsoredDisplaysReportAdGroupsStream,
    SponsoredDisplaysReportCampaignsStream,
    SponsoredDisplaysReportProductAdsStream,
    SponsoredDisplaysReportAdGroupsAudiencesStream,
    SponsoredDisplaysReportCampaignsAudiencesStream,
    SponsoredDisplaysReportProductAdsAudiencesStream,

]

__all__ = [
    'ProfilesStream',
    'PortfoliosStream',
    'SponsoredProductsCampaignsStream',
    'SponsoredBrandsCampaignsStream',
    'AdGroupsStream',
    'BiddableKeywordsStream',
    'NegativeKeywordsStream',
    'CampaignNegativeKeywordsStream',
    'ProductAdsStream',

    'SponsoredProductsReportProductAdsStream',
    'SponsoredProductsReportCampaignsStream',
    'SponsoredProductsReportAdGroupsStream',
    'SponsoredProductsReportKeywordsStream',

    'SponsoredBrandsReportKeywordsStream',
    'SponsoredBrandsReportCampaignsStream',
    'SponsoredBrandsReportAdGroupsStream',

    'SponsoredDisplaysAdGroupsStream',
    'SponsoredDisplaysCampaignsStream',
    'SponsoredDisplaysProductAdsStream',

    'SponsoredBrandsVideoReportKeywordsStream',
    'SponsoredBrandsVideoReportCampaignsStream',
    'SponsoredBrandsVideoReportAdGroupsStream',

    'SponsoredDisplaysReportAdGroupsStream',
    'SponsoredDisplaysReportCampaignsStream',
    'SponsoredDisplaysReportProductAdsStream',

]
