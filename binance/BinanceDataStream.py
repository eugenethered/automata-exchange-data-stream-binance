from data.websocket.WebSocketRunner import WebSocketRunner
from exchangerepo.repository.ExchangeRateRepository import ExchangeRateRepository

from binance.message.exchange.rates.BinanceExchangeDataMessageProcessor import BinanceExchangeDataMessageProcessor
from binance.message.exchange.rates.handler.BinanceExchangeDataMessageHandler import BinanceExchangeDataMessageHandler
from binance.message.exchange.rates.transform.BinanceExchangeMessageTransformer import BinanceExchangeMessageTransformer
from binance.message.trade.BinanceTradeDataMessageProcessor import BinanceTradeDataMessageProcessor
from binance.message.trade.handler.BinanceTradeDataMessageHandler import BinanceTradeDataMessageHandler
from binance.message.trade.transform.BinanceTradeMessageTransformer import BinanceTradeMessageTransformer
from binance.payload.BinanceDataPayloadProcessor import BinanceDataPayloadProcessor

PROCESS_MESSAGE = 'PROCESS_MESSAGE'


class BinanceDataStream:

    # todo: need to handle the "listen key" -> for orders
    def __init__(self, url, options):
        self.options = options
        self.message_processor_options = self.parse_message_processor_options()
        self.message_processors = []
        self.streams = []
        self.init_message_processors()
        self.url = self.build_url(url)
        payload_processor = BinanceDataPayloadProcessor(self.message_processors)
        self.ws_runner = WebSocketRunner(self.url, payload_processor)

    def parse_message_processor_options(self):
        return self.options[PROCESS_MESSAGE].split(',')

    def init_message_processors(self):
        self.init_trade_message_processor()
        self.init_exchange_message_processor()

    def init_exchange_message_processor(self):
        if 'exchange' in self.message_processor_options:
            message_transformer = BinanceExchangeMessageTransformer(self.options)
            repository = ExchangeRateRepository(self.options)
            message_handler = BinanceExchangeDataMessageHandler(repository)
            message_processor = BinanceExchangeDataMessageProcessor(message_transformer, message_handler)
            self.message_processors.append(message_processor)
            self.streams.append(message_processor.get_listen_to_stream())

    def init_trade_message_processor(self):
        if 'trade' in self.message_processor_options:
            message_transformer = BinanceTradeMessageTransformer(self.options)
            message_handler = BinanceTradeDataMessageHandler()
            message_processor = BinanceTradeDataMessageProcessor(message_transformer, message_handler)
            self.message_processors.append(message_processor)
            self.streams.append(message_processor.get_listen_to_stream())

    def build_url(self, url):
        streams = '/'.join(self.streams)
        return f'{url}{streams}'

    def receive_data(self):
        self.ws_runner.receive_data()
