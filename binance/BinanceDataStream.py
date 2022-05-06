from data.websocket.WebSocketRunner import WebSocketRunner
from exchangerepo.repository.ExchangeRateRepository import ExchangeRateRepository

from binance.message.exchange.rates.BinanceExchangeDataMessageProcessor import BinanceExchangeDataMessageProcessor
from binance.message.exchange.rates.handler.BinanceExchangeDataMessageHandler import BinanceExchangeDataMessageHandler
from binance.message.exchange.rates.transform.BinanceExchangeMessageTransformer import BinanceExchangeMessageTransformer
from binance.message.trade.BinanceTradeDataMessageProcessor import BinanceTradeDataMessageProcessor
from binance.message.trade.handler.BinanceTradeDataMessageHandler import BinanceTradeDataMessageHandler
from binance.message.trade.transform.BinanceTradeMessageTransformer import BinanceTradeMessageTransformer
from binance.payload.BinanceDataPayloadProcessor import BinanceDataPayloadProcessor

PROCESS_MESSAGES = 'PROCESS_MESSAGES'


class BinanceDataStream:

    def __init__(self, url, options):
        # todo: build url from streams (listen to specific streams)
        self.url = url
        self.options = options
        self.message_processors = []
        self.init_message_processors()
        payload_processor = BinanceDataPayloadProcessor(self.message_processors)
        self.ws_runner = WebSocketRunner(self.url, payload_processor)

    def init_message_processors(self):
        self.init_trade_message_processor()
        self.init_exchange_message_processor()

    def init_exchange_message_processor(self):
        if 'exchange' in self.options[PROCESS_MESSAGES]:
            message_transformer = BinanceExchangeMessageTransformer(self.options)
            repository = ExchangeRateRepository(self.options)
            message_handler = BinanceExchangeDataMessageHandler(repository)
            message_processor = BinanceExchangeDataMessageProcessor(message_transformer, message_handler)
            self.message_processors.append(message_processor)

    def init_trade_message_processor(self):
        if 'trade' in self.options[PROCESS_MESSAGES]:
            message_transformer = BinanceTradeMessageTransformer(self.options)
            message_handler = BinanceTradeDataMessageHandler()
            message_processor = BinanceTradeDataMessageProcessor(message_transformer, message_handler)
            self.message_processors.append(message_processor)

    def receive_data(self):
        self.ws_runner.receive_data()
