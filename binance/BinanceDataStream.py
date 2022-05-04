from data.websocket.WebSocketRunner import WebSocketRunner
from exchangerepo.repository.ExchangeRateRepository import ExchangeRateRepository

from binance.message.exchange.rates.BinanceExchangeDataMessageProcessor import BinanceExchangeDataMessageProcessor
from binance.message.exchange.rates.handler.BinanceExchangeDataMessageHandler import BinanceExchangeDataMessageHandler
from binance.message.exchange.rates.transform.BinanceExchangeMessageTransformer import BinanceExchangeMessageTransformer
from binance.payload.BinanceDataPayloadProcessor import BinanceDataPayloadProcessor


class BinanceDataStream:

    def __init__(self, url, options):
        self.url = url
        self.options = options
        message_transformer = BinanceExchangeMessageTransformer(self.options)
        repository = ExchangeRateRepository(self.options)
        message_handler = BinanceExchangeDataMessageHandler(repository)
        message_processor = BinanceExchangeDataMessageProcessor(message_transformer, message_handler)
        payload_processor = BinanceDataPayloadProcessor(message_processor)
        self.ws_runner = WebSocketRunner(self.url, payload_processor)

    def receive_data(self):
        self.ws_runner.receive_data()
