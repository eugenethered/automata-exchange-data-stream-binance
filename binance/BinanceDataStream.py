from data.websocket.WebSocketRunner import WebSocketRunner

from binance.message.BinanceDataMessageHandler import BinanceDataMessageHandler
from binance.message.BinanceDataMessageProcessor import BinanceDataMessageProcessor
from binance.message.transform.BinanceMessageTransformer import BinanceMessageTransformer
from binance.payload.BinanceDataPayloadProcessor import BinanceDataPayloadProcessor


class BinanceDataStream:

    def __init__(self, url, options):
        self.url = url
        self.options = options
        message_handler = BinanceDataMessageHandler()
        message_transformer = BinanceMessageTransformer(self.options)
        message_processor = BinanceDataMessageProcessor(message_handler, message_transformer)
        payload_processor = BinanceDataPayloadProcessor(message_processor)
        self.ws_runner = WebSocketRunner(self.url, payload_processor)

    def receive_data(self):
        self.ws_runner.receive_data()
