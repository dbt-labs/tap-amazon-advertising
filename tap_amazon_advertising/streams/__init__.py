
from tap_amazon_advertising.streams.portfolios import PortfoliosStream
from tap_amazon_advertising.streams.sponsored_display_campaigns import SponsoredDisplayCampaignsStream
from tap_amazon_advertising.streams.sponsored_products_campaigns import SponsoredProductsCampaignsStream
from tap_amazon_advertising.streams.sponsored_brands_campaigns import SponsoredBrandsCampaignsStream
from tap_amazon_advertising.streams.ad_groups import AdGroupsStream
from tap_amazon_advertising.streams.biddable_keywords import BiddableKeywordsStream
from tap_amazon_advertising.streams.negative_keywords import NegativeKeywordsStream
from tap_amazon_advertising.streams.campaign_negative_keywords import CampaignNegativeKeywordsStream
from tap_amazon_advertising.streams.product_ads import ProductAdsStream

from tap_amazon_advertising.streams.sponsored_display_report import SponsoredDisplayReportProductAdsStream, \
        SponsoredDisplayReportCampaignsStream, \
        SponsoredDisplayReportAdGroupsStream

from tap_amazon_advertising.streams.sponsored_products_report import SponsoredProductsReportProductAdsStream, \
        SponsoredProductsReportCampaignsStream, \
        SponsoredProductsReportAdGroupsStream, \
        SponsoredProductsReportKeywordsStream

from tap_amazon_advertising.streams.sponsored_brands_report import SponsoredBrandsReportKeywordsStream, \
        SponsoredBrandsReportCampaignsStream, \
        SponsoredBrandsReportAdGroupsStream


AVAILABLE_STREAMS = [
    PortfoliosStream,
    SponsoredDisplayCampaignsStream,
    SponsoredProductsCampaignsStream,
    # SponsoredBrandsCampaignsStream,
    AdGroupsStream,
    BiddableKeywordsStream,
    NegativeKeywordsStream,
    CampaignNegativeKeywordsStream,
    ProductAdsStream,

    # SD Reports
    SponsoredDisplayReportProductAdsStream,
    SponsoredDisplayReportCampaignsStream,
    SponsoredDisplayReportAdGroupsStream,

    # SP Reports
    SponsoredProductsReportProductAdsStream,
    SponsoredProductsReportCampaignsStream,
    SponsoredProductsReportAdGroupsStream,
    SponsoredProductsReportKeywordsStream,

    # SB Reports
    # SponsoredBrandsReportKeywordsStream,
    # SponsoredBrandsReportCampaignsStream,
    # SponsoredBrandsReportAdGroupsStream,
]

__all__ = [
    'PortfoliosStream',
    'SponsoredProductsCampaignsStream',
    'SponsoredBrandsCampaignsStream',
    'AdGroupsStream',
    'BiddableKeywordsStream',
    'NegativeKeywordsStream',
    'CampaignNegativeKeywordsStream',
    'ProductAdsStream',

    'SponsoredDisplayReportProductAdsStream',
    'SponsoredDisplayReportCampaignsStream',
    'SponsoredDisplayReportAdGroupsStream',

    'SponsoredProductsReportProductAdsStream',
    'SponsoredProductsReportCampaignsStream',
    'SponsoredProductsReportAdGroupsStream',
    'SponsoredProductsReportKeywordsStream',

    'SponsoredBrandsReportKeywordsStream',
    'SponsoredBrandsReportCampaignsStream',
    'SponsoredBrandsReportAdGroupsStream',
]
