
import singer

from dateutil.parser import parse

LOGGER = singer.get_logger()  # noqa


def get_config_start_date(config):
    return parse(config.get('start_date')).date()
