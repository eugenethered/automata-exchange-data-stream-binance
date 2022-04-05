from data.message.DataMessageProcessor import DataMessageProcessor
from utility.json_utility import as_data

from binance.message.BinanceDataMessageHandler import BinanceDataMessageHandler
from binance.message.transform.BinanceMessageTransformer import BinanceMessageTransformer


class BinanceDataMessageProcessor(DataMessageProcessor):

    def __init__(self, message_handler: BinanceDataMessageHandler, message_transformer: BinanceMessageTransformer):
        self.message_handler = message_handler
        self.message_transformer = message_transformer

    def process_message(self, message):
        symbol = as_data(message, 's')
        price = as_data(message, 'c')
        event_time = as_data(message, 'E')
        exchange_rate = self.message_transformer.transform(symbol, price)
        if exchange_rate is not None:
            self.message_handler.handle_message(exchange_rate, event_time)
