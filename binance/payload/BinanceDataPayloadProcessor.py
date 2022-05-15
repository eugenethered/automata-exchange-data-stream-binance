import logging
import time
from typing import List

from config.report.holder.ConfigReporterHolder import ConfigReporterHolder
from coreutility.collection.dictionary_utility import as_data
from coreutility.json.json_utility import as_json
from data.message.DataMessageProcessor import DataMessageProcessor
from data.payload.DataPayloadProcessor import DataPayloadProcessor


class BinanceDataPayloadProcessor(DataPayloadProcessor):

    def __init__(self, message_processors: List[DataMessageProcessor]):
        self.message_processors = message_processors

    def process_payload(self, payload):
        start_time = time.perf_counter()

        json_data = as_json(payload)
        logging.debug(f'payload received:{json_data}')
        stream = as_data(json_data, 'stream')
        payload_data = as_data(json_data, 'data')
        self.process_payload_messages(payload_data, stream)

        end_time = time.perf_counter()
        logging.info(f'processed payload in {end_time - start_time:0.4f} seconds')

    def process_payload_messages(self, payload_data, stream):
        for message in payload_data:
            self.process_payload_message(message, stream)
        self.post_payload_process()

    def process_payload_message(self, payload_message, stream):
        for message_processor in self.message_processors:
            if message_processor.get_listen_stream() == stream:
                message_processor.process_message(payload_message)

    @staticmethod
    def post_payload_process():
        logging.debug('post payload processing')
        ConfigReporterHolder().delay_missing_storing()
