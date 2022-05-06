from data.websocket.WebSocketRunner import WebSocketRunner
from exchangerepo.repository.ExchangeRateRepository import ExchangeRateRepository

from binance.message.exchange.rates.BinanceExchangeDataMessageProcessor import BinanceExchangeDataMessageProcessor
from binance.message.exchange.rates.handler.BinanceExchangeDataMessageHandler import BinanceExchangeDataMessageHandler
from binance.message.exchange.rates.transform.BinanceExchangeMessageTransformer import BinanceExchangeMessageTransformer
from binance.message.trade.BinanceTradeDataMessageProcessor import BinanceTradeDataMessageProcessor
from binance.message.trade.handler.BinanceTradeDataMessageHandler import BinanceTradeDataMessageHandler
from binance.message.trade.transform.BinanceTradeMessageTransformer import BinanceTradeMessageTransformer
from binance.payload.BinanceDataPayloadProcessor import BinanceDataPayloadProcessor


class BinanceDataStream:

    def __init__(self, url, options):
        # todo: build url from streams (listen to specific streams)
        self.url = url
        self.options = options
        message_processors = self.init_message_processors()
        payload_processor = BinanceDataPayloadProcessor(message_processors)
        self.ws_runner = WebSocketRunner(self.url, payload_processor)

    def init_message_processors(self):
        trade_message_processor = self.init_trade_message_processor()
        exchange_message_processor = self.init_exchange_message_processor()
        return [exchange_message_processor, trade_message_processor]

    def init_exchange_message_processor(self):
        message_transformer = BinanceExchangeMessageTransformer(self.options)
        repository = ExchangeRateRepository(self.options)
        message_handler = BinanceExchangeDataMessageHandler(repository)
        return BinanceExchangeDataMessageProcessor(message_transformer, message_handler)

    def init_trade_message_processor(self):
        message_transformer = BinanceTradeMessageTransformer(self.options)
        message_handler = BinanceTradeDataMessageHandler()
        return BinanceTradeDataMessageProcessor(message_transformer, message_handler)

    def receive_data(self):
        self.ws_runner.receive_data()
