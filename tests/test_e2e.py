"""
End to end integration tests for the tap.
"""
import pytest
from integrations_testing_framework import *

import tap_amazon_advertising

# Config file
CONFIG_FILE = 'config.json'
# Streams file
STREAMS_FILE = 'tests/all-streams.json'
# Directories
CONFIGS_DIR = 'tests/configs/'
REQUESTS_DIR = 'tests/requests/'
RESPONSES_DIR = 'tests/responses/'
RECORDING_CONF = {
    'filter_req_data': ['client_id', 'client_secret', 'refresh_token'],
    'filter_req_headers': ['Authorization', 'Amazon-Advertising-API-ClientId', 'Amazon-Advertising-API-Scope'],
    'filter_resp_data_except': ['id', 'scope', 'status', 'statusDetails', 'location', 'last_record', 'reportId']
}


@assert_stdout_matches(STREAMS_FILE)
@intercept_requests(os.path.join(REQUESTS_DIR, 'discovery.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--discover'])
def test_discovery():
    """
    Test tap discover function.
    """
    tap_amazon_advertising.main()


@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'ad_group_biddable_keywords.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'ad_group_biddable_keywords.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'ad_group_biddable_keywords',
                                                                          stream_key='stream')])
def test_stream_ad_group_biddable_keywords():
    """
    Test stream 'ad_group_biddable_keywords'.
    """
    tap_amazon_advertising.main()


@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'ad_group_negative_keywords.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'ad_group_negative_keywords.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'ad_group_negative_keywords',
                                                                          stream_key='stream')])
def test_stream_ad_group_negative_keywords():
    """
    Test stream 'ad_group_negative_keywords'.
    """
    tap_amazon_advertising.main()


@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'ad_groups.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'ad_groups.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'ad_groups',
                                                                          stream_key='stream')])
def test_stream_ad_groups():
    """
    Test stream 'ad_groups'.
    """
    tap_amazon_advertising.main()


@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'campaign_negative_keywords.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'campaign_negative_keywords.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'campaign_negative_keywords',
                                                                          stream_key='stream')])
def test_stream_campaign_negative_keywords():
    """
    Test stream 'campaign_negative_keywords'.
    """
    tap_amazon_advertising.main()


@pytest.mark.skip('No data available for the stream')
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'portfolios.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'portfolios.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'portfolios',
                                                                          stream_key='stream')])
def test_stream_portfolios():
    """
    Test stream 'portfolios'.
    """
    tap_amazon_advertising.main()


@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'product_ads.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'product_ads.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'product_ads',
                                                                          stream_key='stream')])
def test_stream_product_ads():
    """
    Test stream 'product_ads'.
    """
    tap_amazon_advertising.main()


@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'profiles.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'profiles.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'profiles',
                                                                          stream_key='stream')])
def test_stream_profiles():
    """
    Test stream 'profiles'.
    """
    tap_amazon_advertising.main()


@pytest.mark.skip('No data available, timed out')
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'sponsored_brands_report_ad_groups.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'sponsored_brands_report_ad_groups.txt'),
                    generate=False,
                    **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'sponsored_brands_report_ad_groups',
                                                                          stream_key='stream')])
def test_stream_sponsored_brands_report_ad_groups():
    """
    Test stream 'sponsored_brands_report_ad_groups'.
    """
    tap_amazon_advertising.main()


@pytest.mark.skip('No data available, timed out')
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'sponsored_brands_report_campaigns.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'sponsored_brands_report_campaigns.txt'),
                    generate=False,
                    **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'sponsored_brands_report_campaigns',
                                                                          stream_key='stream')])
def test_stream_sponsored_brands_report_campaigns():
    """
    Test stream 'sponsored_brands_report_campaigns'.
    """
    tap_amazon_advertising.main()


@pytest.mark.skip('No data available, timed out')
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'sponsored_brands_report_keywords.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'sponsored_brands_report_keywords.txt'),
                    generate=False,
                    **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'sponsored_brands_report_keywords',
                                                                          stream_key='stream')])
def test_stream_sponsored_brands_report_keywords():
    """
    Test stream 'sponsored_brands_report_keywords'.
    """
    tap_amazon_advertising.main()


@pytest.mark.skip('No data available, timed out')
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'sponsored_brands_video_report_ad_groups.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'sponsored_brands_video_report_ad_groups.txt'),
                    generate=False,
                    **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'sponsored_brands_video_report_ad_groups',
                                                                          stream_key='stream')])
def test_stream_sponsored_brands_video_report_ad_groups():
    """
    Test stream 'sponsored_brands_video_report_ad_groups'.
    """
    tap_amazon_advertising.main()


@pytest.mark.skip('No data available, timed out')
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'sponsored_brands_video_report_campaigns.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'sponsored_brands_video_report_campaigns.txt'),
                    generate=False,
                    **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'sponsored_brands_video_report_campaigns',
                                                                          stream_key='stream')])
def test_stream_sponsored_brands_video_report_campaigns():
    """
    Test stream 'sponsored_brands_video_report_campaigns'.
    """
    tap_amazon_advertising.main()


@pytest.mark.skip('No data available, timed out')
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'sponsored_brands_video_report_keywords.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'sponsored_brands_video_report_keywords.txt'),
                    generate=False,
                    **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'sponsored_brands_video_report_keywords',
                                                                          stream_key='stream')])
def test_stream_sponsored_brands_video_report_keywords():
    """
    Test stream 'sponsored_brands_video_report_keywords'.
    """
    tap_amazon_advertising.main()


@pytest.mark.skip('No data available for the stream')
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'sponsored_displays_ad_groups.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'sponsored_displays_ad_groups.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'sponsored_displays_ad_groups',
                                                                          stream_key='stream')])
def test_stream_sponsored_displays_ad_groups():
    """
    Test stream 'sponsored_displays_ad_groups'.
    """
    tap_amazon_advertising.main()


@pytest.mark.skip('No data available for the stream')
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'sponsored_displays_campaigns.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'sponsored_displays_campaigns.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'sponsored_displays_campaigns',
                                                                          stream_key='stream')])
def test_stream_sponsored_displays_campaigns():
    """
    Test stream 'sponsored_displays_campaigns'.
    """
    tap_amazon_advertising.main()


@pytest.mark.skip('No data available for the stream')
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'sponsored_displays_product_ads.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'sponsored_displays_product_ads.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'sponsored_displays_product_ads',
                                                                          stream_key='stream')])
def test_stream_sponsored_displays_product_ads():
    """
    Test stream 'sponsored_displays_product_ads'.
    """
    tap_amazon_advertising.main()


@pytest.mark.skip('No data available, timed out')
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'sponsored_displays_report_ad_groups.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'sponsored_displays_report_ad_groups.txt'),
                    generate=False,
                    **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'sponsored_displays_report_ad_groups',
                                                                          stream_key='stream')])
def test_stream_sponsored_displays_report_ad_groups():
    """
    Test stream 'sponsored_displays_report_ad_groups'.
    """
    tap_amazon_advertising.main()


@pytest.mark.skip('No data available, timed out')
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'sponsored_displays_report_ad_groups_audiences.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'sponsored_displays_report_ad_groups_audiences.txt'),
                    generate=False,
                    **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'sponsored_displays_report_ad_groups_audiences',
                                                                          stream_key='stream')])
def test_stream_sponsored_displays_report_ad_groups_audiences():
    """
    Test stream 'sponsored_displays_report_ad_groups_audiences'.
    """
    tap_amazon_advertising.main()


@pytest.mark.skip('No data available, timed out')
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'sponsored_displays_report_campaigns.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'sponsored_displays_report_campaigns.txt'),
                    generate=False,
                    **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'sponsored_displays_report_campaigns',
                                                                          stream_key='stream')])
def test_stream_sponsored_displays_report_campaigns():
    """
    Test stream 'sponsored_displays_report_campaigns'.
    """
    tap_amazon_advertising.main()


@pytest.mark.skip('No data available, timed out')
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'sponsored_displays_report_campaigns_audiences.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'sponsored_displays_report_campaigns_audiences.txt'),
                    generate=False,
                    **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'sponsored_displays_report_campaigns_audiences',
                                                                          stream_key='stream')])
def test_stream_sponsored_displays_report_campaigns_audiences():
    """
    Test stream 'sponsored_displays_report_campaigns_audiences'.
    """
    tap_amazon_advertising.main()



@pytest.mark.skip('No data available, timed out')
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'sponsored_displays_report_product_ads.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'sponsored_displays_report_product_ads.txt'),
                    generate=False,
                    **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'sponsored_displays_report_product_ads',
                                                                          stream_key='stream')])
def test_stream_sponsored_displays_report_product_ads():
    """
    Test stream 'sponsored_displays_report_product_ads'.
    """
    tap_amazon_advertising.main()


@pytest.mark.skip('No data available, timed out')
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'sponsored_displays_report_product_ads_audiences.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'sponsored_displays_report_product_ads_audiences.txt'),
                    generate=False,
                    **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'sponsored_displays_report_product_ads_audiences',
                                                                          stream_key='stream')])
def test_stream_sponsored_displays_report_product_ads_audiences():
    """
    Test stream 'sponsored_displays_report_product_ads_audiences'.
    """
    tap_amazon_advertising.main()


@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'sponsored_products_campaigns.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'sponsored_products_campaigns.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'sponsored_products_campaigns',
                                                                          stream_key='stream')])
def test_stream_sponsored_products_campaigns():
    """
    Test stream 'sponsored_products_campaigns'.
    """
    tap_amazon_advertising.main()


@pytest.mark.skip('Takes too long to complete')
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'sponsored_products_report_ad_groups.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'sponsored_products_report_ad_groups.txt'),
                    generate=False,
                    **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'sponsored_products_report_ad_groups',
                                                                          stream_key='stream')])
def test_stream_sponsored_products_report_ad_groups():
    """
    Test stream 'sponsored_products_report_ad_groups'.
    """
    tap_amazon_advertising.main()


@pytest.mark.skip('Takes too long to complete')
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'sponsored_products_report_campaigns.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'sponsored_products_report_campaigns.txt'),
                    generate=False,
                    **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'sponsored_products_report_campaigns',
                                                                          stream_key='stream')])
def test_stream_sponsored_products_report_campaigns():
    """
    Test stream 'sponsored_products_report_campaigns'.
    """
    tap_amazon_advertising.main()


@pytest.mark.skip('Takes too long to complete')
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'sponsored_products_report_keywords.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'sponsored_products_report_keywords.txt'),
                    generate=False,
                    **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'sponsored_products_report_keywords',
                                                                          stream_key='stream')])
def test_stream_sponsored_products_report_keywords():
    """
    Test stream 'sponsored_products_report_keywords'.
    """
    tap_amazon_advertising.main()


@pytest.mark.skip('Takes too long to complete')
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'sponsored_products_report_product_ads.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'sponsored_products_report_product_ads.txt'),
                    generate=False,
                    **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--catalog', utils.select_schema(STREAMS_FILE,
                                                                          'sponsored_products_report_product_ads',
                                                                          stream_key='stream')])
def test_stream_sponsored_products_report_product_ads():
    """
    Test stream 'sponsored_products_report_product_ads'.
    """
    tap_amazon_advertising.main()
