import math
import pytz
import singer
import singer.utils
import singer.metrics
import time
import datetime

from tap_amazon_advertising.config import get_config_start_date
from tap_amazon_advertising.state import incorporate, save_state, \
    get_last_record_value_for_table

from tap_framework.streams import BaseStream as base

LOGGER = singer.get_logger()

BASE_URL = 'https://advertising-api.amazon.com'

class BaseStream(base):
    KEY_PROPERTIES = ['id']

    def get_params(self):
        return {}

    def get_body(self):
        return {}

    def get_url(self, path):
        return '{}{}'.format(BASE_URL, path)

    def transform_record(self, record, inject_profile=True):
        if inject_profile:
            record['profileId'] = self.config.get('profile_id')
        transformed = base.transform_record(self, record)

        return transformed

    def sync_data(self):
        table = self.TABLE
        LOGGER.info('Syncing data for entity {}'.format(table))

        url = self.get_url(self.api_path)
        params = self.get_params()
        body = self.get_body()

        result = self.client.make_request(
            url, self.API_METHOD, params=params, body=body)
        data = self.get_stream_data(result)

        with singer.metrics.record_counter(endpoint=table) as counter:
            for obj in data:
                singer.write_records(
                    table,
                    [obj])

                counter.increment()
        return self.state

class PaginatedStream(BaseStream):
    def get_params(self, index, count):
        return {
            "startIndex": index,
            "count": count
        }

    def sync_data(self):
        table = self.TABLE
        LOGGER.info('Syncing data for entity {}'.format(table))

        url = self.get_url(self.api_path)
        body = self.get_body()

        index = 0
        count = 5000
        while True:
            LOGGER.info('Syncing {} rows from index {}'.format(count, index))

            params = self.get_params(index, count)
            result = self.client.make_request(
                url, self.API_METHOD, params=params, body=body)

            data = self.get_stream_data(result)
            if len(data) == 0:
                break
            else:
                index += count

            with singer.metrics.record_counter(endpoint=table) as counter:
                for obj in data:
                    singer.write_records(
                        table,
                        [obj])

                    counter.increment()

        return self.state


class ReportStream(BaseStream):
    def create_report(self, url, day):
        body = self.get_body(day)

        # Create a report
        report = self.client.make_request(url, 'POST', body=body)
        report_id = report['reportId']

        # If we don't sleep here, then something funky happens and the API
        # takes _significantly_ longer to return a SUCCESS status
        time.sleep(3)
        LOGGER.info("Polling")
        report_url = '{}/v2/reports/{}'.format(BASE_URL, report_id)

        num_polls = 7
        for i in range(num_polls):
            poll = self.client.make_request(report_url, 'GET')
            status = poll['status']
            LOGGER.info("Poll {} of {}, status={}".format(i+1, num_polls, status))

            if status == 'SUCCESS':
                return poll['location']
            else:
                timeout = (1 + i) ** 2
                LOGGER.info("In state: {}, Sleeping for {} seconds".format(status, timeout))
                time.sleep(timeout)

        LOGGER.info("Unable to sync from {} for day {}-- moving on".format(url, day))

    def sync_data(self):
        table = self.TABLE
        LOGGER.info('Syncing data for entity {}'.format(table))

        yesterday = datetime.date.today() - datetime.timedelta(days=1)

        sync_date = get_last_record_value_for_table(self.state, table)
        if sync_date is None:
            sync_date = get_config_start_date(self.config)

        # Add a lookback to refresh attribution metrics for more recent orders
        # Removed as Amazon API does not allow to get data older than 60 days
        # and it's using another value for start_date
        #sync_date -= datetime.timedelta(days=self.config.get('lookback', 30))

        while sync_date <= yesterday:
            LOGGER.info("Syncing {} for date {}".format(table, sync_date))

            url = self.get_url(self.api_path)
            report_url = self.create_report(url, sync_date)

            if report_url is None:
                break

            result = self.client.download_gzip(report_url)
            data = self.get_stream_data(result, sync_date)

            with singer.metrics.record_counter(endpoint=table) as counter:
                for obj in data:
                    singer.write_records(
                        table,
                        [obj])

                    counter.increment()


            self.state = incorporate(self.state, self.TABLE,
                                     'last_record', sync_date.isoformat())
            save_state(self.state)

            sync_date += datetime.timedelta(days=1)

        return self.state
