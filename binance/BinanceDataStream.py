from data.websocket.WebSocketRunner import WebSocketRunner

from binance.payload.BinanceDataPayloadProcessor import BinanceDataPayloadProcessor


class BinanceDataStream:

    def __init__(self):
        # todo: pass these via arguments
        url = 'wss://testnet.binance.vision/stream?streams=!ticker@arr'
        payload_processor = BinanceDataPayloadProcessor()
        self.ws_runner = WebSocketRunner(url, payload_processor)

    def receive_data(self):
        self.ws_runner.receive_data()
