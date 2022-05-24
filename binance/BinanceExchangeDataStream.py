from data.websocket.WebSocketRunner import WebSocketRunner
from exchangerepo.repository.ExchangeRateRepository import ExchangeRateRepository
from exchangetransformrepo.repository.ExchangeTransformRepository import ExchangeTransformRepository
from processmanager.ProcessBase import ProcessBase

from binance.message.exchange.rates.BinanceExchangeDataMessageProcessor import BinanceExchangeDataMessageProcessor
from binance.message.exchange.rates.handler.BinanceExchangeDataMessageHandler import BinanceExchangeDataMessageHandler
from binance.message.exchange.rates.transform.BinanceExchangeMessageTransformer import BinanceExchangeMessageTransformer
from binance.payload.BinanceDataPayloadProcessor import BinanceDataPayloadProcessor


class BinanceExchangeDataStream(ProcessBase):

    def __init__(self, url, options):
        super().__init__(options, 'binance', 'exchange-data-stream')
        self.url = url
        self.options = options
        exchange_message_processor = self.init_exchange_message_processor()
        payload_processor = BinanceDataPayloadProcessor([exchange_message_processor])
        self.ws_runner = WebSocketRunner(self.url, payload_processor, ping_interval=8)
        self.init_web_socket_callbacks()

    def init_web_socket_callbacks(self):
        self.ws_runner.set_stopped_callback(self.process_stopped)
        self.ws_runner.set_running_callback(self.process_running)

    def init_exchange_message_processor(self):
        repository = ExchangeTransformRepository(self.options)
        message_transformer = BinanceExchangeMessageTransformer(repository)
        repository = ExchangeRateRepository(self.options)
        message_handler = BinanceExchangeDataMessageHandler(repository)
        return BinanceExchangeDataMessageProcessor(message_transformer, message_handler)

    def receive_data(self):
        self.ws_runner.receive_data()
