from data.message.DataMessageProcessor import DataMessageProcessor
from utility.json_utility import as_data

from binance.message.exchange.rates.handler.BinanceExchangeDataMessageHandler import BinanceExchangeDataMessageHandler
from binance.message.exchange.rates.transform import BinanceExchangeMessageTransformer


class BinanceExchangeDataMessageProcessor(DataMessageProcessor):

    def __init__(self, message_transformer: BinanceExchangeMessageTransformer, message_handler: BinanceExchangeDataMessageHandler):
        super().__init__('!ticker@arr')
        self.message_transformer = message_transformer
        self.message_handler = message_handler

    def process_message(self, message):
        symbol = as_data(message, 's')
        price = as_data(message, 'c')
        event_time = as_data(message, 'E')
        exchange_rate = self.message_transformer.transform(symbol, price)
        self.message_handler.handle_exchange_rate(exchange_rate, event_time)
