import logging

from binance.message.exchange.rates.BinanceExchangeDataMessageProcessor import BinanceExchangeDataMessageProcessor
from data.payload.DataPayloadProcessor import DataPayloadProcessor
from utility.json_utility import as_json, as_data


class BinanceDataPayloadProcessor(DataPayloadProcessor):

    # todo: change to use multiple processors
    def __init__(self, message_processor: BinanceExchangeDataMessageProcessor):
        self.message_processor = message_processor

    def process_payload(self, payload):
        json_data = as_json(payload)
        # todo: get the stream
        logging.debug(f'Payload received:{json_data}')
        payload_data = as_data(json_data, 'data')
        for message in payload_data:
            self.process_payload_messages(message)

    def process_payload_messages(self, payload_message):
        self.message_processor.process_message(payload_message)
