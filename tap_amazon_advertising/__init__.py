#!/usr/bin/env python3

import singer
import re
import os

import tap_framework

from tap_amazon_advertising.client import AmazonAdvertisingClient
from tap_amazon_advertising.streams import AVAILABLE_STREAMS

LOGGER = singer.get_logger()  # noqa

REQUIRED_CONFIG_KEYS = ['client_id', 'client_secret', 'refresh_token', 'redirect_uri', 'start_date', 'profiles']

def expand_env(config):
    assert isinstance(config, dict)

    def repl(match):
        env_key = match.group(1)
        return os.environ.get(env_key, "")

    def expand(v):
        assert not isinstance(v, dict)
        if isinstance(v, str):
            return re.sub(r"env\[(\w+)\]", repl, v)
        else:
            return v

    copy = {}
    for k, v in config.items():
        if isinstance(v, dict):
            copy[k] = expand_env(v)
        elif isinstance(v, list):
            copy[k] = [expand_env(x) if isinstance(
                x, dict) else expand(x) for x in v]
        else:
            copy[k] = expand(v)

    return copy

class AmazonAdvertisingRunner(tap_framework.Runner):
    pass


@singer.utils.handle_top_exception(LOGGER)
def main():
    args = singer.utils.parse_args(required_config_keys=REQUIRED_CONFIG_KEYS)

    if not args.discover:
        args.config = expand_env(args.config)

    client = AmazonAdvertisingClient(args.config)

    runner = AmazonAdvertisingRunner(
        args, client, AVAILABLE_STREAMS)

    if args.discover:
        runner.do_discover()
    else:
        runner.do_sync()


if __name__ == '__main__':
    main()
