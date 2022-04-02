from data.websocket.WebSocketRunner import WebSocketRunner

from binance.message.BinanceDataMessageHandler import BinanceDataMessageHandler
from binance.message.BinanceDataMessageProcessor import BinanceDataMessageProcessor
from binance.payload.BinanceDataPayloadProcessor import BinanceDataPayloadProcessor


class BinanceDataStream:

    def __init__(self):
        # todo: pass these via arguments
        url = 'wss://testnet.binance.vision/stream?streams=!ticker@arr'
        message_handler = BinanceDataMessageHandler()
        message_processor = BinanceDataMessageProcessor(message_handler)
        payload_processor = BinanceDataPayloadProcessor(message_processor)
        self.ws_runner = WebSocketRunner(url, payload_processor)

    def receive_data(self):
        self.ws_runner.receive_data()
