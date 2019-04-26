import math
import pytz
import singer
import singer.utils
import singer.metrics
import time
import datetime

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

        LOGGER.info("Polling")
        report_url = '{}/v2/reports/{}'.format(BASE_URL, report_id)

        num_polls = 10
        for i in range(num_polls):
            poll = self.client.make_request(report_url, 'GET')
            status = poll['status']
            LOGGER.info("Poll {} of {}, status={}".format(i+1, num_polls, status))

            if status == 'SUCCESS':
                return poll['location']
            else:
                timeout = (1 + i) ** 2
                LOGGER.info("Sleeping for {} seconds".format(timeout))
                time.sleep(timeout)

        raise RuntimeError("Could not fetch report for day {} from url {}".format(day, url))

    def sync_data(self):
        table = self.TABLE
        LOGGER.info('Syncing data for entity {}'.format(table))

        today = datetime.date.today()
        looback = datetime.timedelta(days=self.config.get('sync_lookback', 30))

        sync_date = today - looback
        while sync_date <= today:
            url = self.get_url(self.api_path)
            report_url = self.create_report(url, sync_date)

            result = self.client.download_gzip(report_url)
            data = self.get_stream_data(result, sync_date)

            with singer.metrics.record_counter(endpoint=table) as counter:
                for obj in data:
                    singer.write_records(
                        table,
                        [obj])

                    counter.increment()

            sync_date += datetime.timedelta(days=1)

        return self.state
