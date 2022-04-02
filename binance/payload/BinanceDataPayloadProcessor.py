from data.message.DataMessageProcessor import DataMessageProcessor
from data.payload.DataPayloadProcessor import DataPayloadProcessor

from utility.json_utility import as_json


class BinanceDataPayloadProcessor(DataPayloadProcessor):

    def __init__(self, message_processor: DataMessageProcessor):
        self.message_processor = message_processor

    def process_payload(self, payload):
        json_data = as_json(payload)
        if 'data' in json_data:
            payload_data = json_data['data']
            for message in payload_data:
                self.process_payload_messages(message)

    def process_payload_messages(self, payload_message):
        self.message_processor.process_message(payload_message)
