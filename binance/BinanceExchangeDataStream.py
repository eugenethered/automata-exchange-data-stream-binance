from data.websocket.WebSocketRunner import WebSocketRunner
from exchangerepo.repository.ExchangeRateRepository import ExchangeRateRepository

from binance.message.exchange.rates.BinanceExchangeDataMessageProcessor import BinanceExchangeDataMessageProcessor
from binance.message.exchange.rates.handler.BinanceExchangeDataMessageHandler import BinanceExchangeDataMessageHandler
from binance.message.exchange.rates.transform.BinanceExchangeMessageTransformer import BinanceExchangeMessageTransformer
from binance.payload.BinanceDataPayloadProcessor import BinanceDataPayloadProcessor


class BinanceExchangeDataStream:

    def __init__(self, url, options):
        self.url = url
        self.options = options
        exchange_message_processor = self.init_exchange_message_processor()
        payload_processor = BinanceDataPayloadProcessor([exchange_message_processor])
        self.ws_runner = WebSocketRunner(self.url, payload_processor)

    def init_exchange_message_processor(self):
        message_transformer = BinanceExchangeMessageTransformer(self.options)
        repository = ExchangeRateRepository(self.options)
        message_handler = BinanceExchangeDataMessageHandler(repository)
        return BinanceExchangeDataMessageProcessor(message_transformer, message_handler)

    def receive_data(self):
        self.ws_runner.receive_data()