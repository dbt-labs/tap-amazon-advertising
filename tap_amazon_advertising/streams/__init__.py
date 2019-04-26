
from tap_amazon_advertising.streams.profiles import ProfilesStream
from tap_amazon_advertising.streams.portfolios import PortfoliosStream
from tap_amazon_advertising.streams.campaigns import CampaignsStream
from tap_amazon_advertising.streams.ad_groups import AdGroupsStream
from tap_amazon_advertising.streams.biddable_keywords import BiddableKeywordsStream
from tap_amazon_advertising.streams.negative_keywords import NegativeKeywordsStream
from tap_amazon_advertising.streams.campaign_negative_keywords import CampaignNegativeKeywordsStream
from tap_amazon_advertising.streams.product_ads import ProductAdsStream

from tap_amazon_advertising.streams.sponsored_products_report import SponsoredProductsReportProductAdsStream
from tap_amazon_advertising.streams.sponsored_brands_report import SponsoredBrandsReportKeywordsStream

AVAILABLE_STREAMS = [
    ProfilesStream,
    PortfoliosStream,
    CampaignsStream,
    AdGroupsStream,
    BiddableKeywordsStream,
    NegativeKeywordsStream,
    CampaignNegativeKeywordsStream,
    ProductAdsStream,

    SponsoredProductsReportProductAdsStream,
    SponsoredBrandsReportKeywordsStream,
]

__all__ = [
    'ProfilesStream',
    'PortfoliosStream',
    'CampaignsStream',
    'AdGroupsStream',
    'BiddableKeywordsStream',
    'NegativeKeywordsStream',
    'CampaignNegativeKeywordsStream',
    'ProductAdsStream',

    'SponsoredProductsReportProductAdsStream',
    'SponsoredBrandsReportKeywordsStream',
]
