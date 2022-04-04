from data.message.DataMessageProcessor import DataMessageProcessor
from utility.json_utility import as_data

from binance.message.BinanceDataMessageHandler import BinanceDataMessageHandler
from binance.message.transform.BinanceMessageTransformer import BinanceMessageTransformer


class BinanceDataMessageProcessor(DataMessageProcessor):

    def __init__(self, message_handler: BinanceDataMessageHandler, options):
        self.message_handler = message_handler
        self.message_transformer = BinanceMessageTransformer(options)

    def process_message(self, message):
        symbol = as_data(message, 's')
        price = as_data(message, 'c')
        exchange_rate = self.message_transformer.transform(symbol, price)
        if exchange_rate is not None:
            self.message_handler.handle_message(exchange_rate)
