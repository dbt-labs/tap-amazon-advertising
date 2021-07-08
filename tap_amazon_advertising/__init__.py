#!/usr/bin/env python3
import json
import sys

import singer

import tap_framework
from singer import metadata

from tap_amazon_advertising.client import AmazonAdvertisingClient
from tap_amazon_advertising.streams import AVAILABLE_STREAMS

LOGGER = singer.get_logger()  # noqa


class AmazonAdvertisingRunner(tap_framework.Runner):
    pass


def do_discover(args):
    LOGGER.info("Starting discovery.")

    catalog = []
    report_streams = [
        "sponsored_products_report_product_ads",
        "sponsored_products_report_campaigns",
        "sponsored_products_report_ad_groups",
        "sponsored_products_report_keywords",
        "sponsored_brands_report_keywords",
        "sponsored_brands_report_campaigns",
        "sponsored_brands_report_ad_groups",
    ]

    for available_stream in AVAILABLE_STREAMS:
        stream = available_stream(args.config, args.state, None, None)

        schemas = stream.generate_catalog()
        for schema in schemas:
            if schema["tap_stream_id"] in report_streams:
                schema['replication_method'] = "INCREMENTAL"
                schema['replication_key'] = "day"
                mdata = schema["metadata"]
                mdata = metadata.to_map(mdata)
                metadata.write(mdata, (), "table-key-properties", schema["key_properties"])
                metadata.write(mdata, (), "forced-replication-method", "INCREMENTAL")
                metadata.write(mdata, (), "valid-replication-keys", ["day"])
                schema['metadata'] = metadata.to_list(mdata)
        catalog += schemas

    json.dump({'streams': catalog}, sys.stdout, indent=4)


@singer.utils.handle_top_exception(LOGGER)
def main():
    args = singer.utils.parse_args(
        required_config_keys=['client_id', 'client_secret', 'refresh_token',
                              'redirect_uri', 'profile_id', 'start_date', 'base_url'])

    client = AmazonAdvertisingClient(args.config)

    runner = AmazonAdvertisingRunner(
        args, client, AVAILABLE_STREAMS)

    if args.discover:
        do_discover(args)
    else:
        runner.do_sync()


if __name__ == '__main__':
    main()
