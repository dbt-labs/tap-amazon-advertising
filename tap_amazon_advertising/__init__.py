#!/usr/bin/env python3

import singer

import tap_framework

from tap_amazon_advertising.client import AmazonAdvertisingClient
from tap_amazon_advertising.streams import AVAILABLE_STREAMS

LOGGER = singer.get_logger()  # noqa


class AmazonAdvertisingRunner(tap_framework.Runner):
    pass


@singer.utils.handle_top_exception(LOGGER)
def main():
    args = singer.utils.parse_args(
        required_config_keys=['client_id', 'client_secret', 'refresh_token',
                              'redirect_uri', 'profile_id', 'start_date'])

    client = AmazonAdvertisingClient(args.config)
    runner = AmazonAdvertisingRunner(
        args, client, AVAILABLE_STREAMS)

    if args.discover:
        runner.do_discover()
    else:
        runner.do_sync()


if __name__ == '__main__':
    main()
