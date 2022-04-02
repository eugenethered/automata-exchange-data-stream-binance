from core.exchange.ExchangeRate import ExchangeRate
from core.number.BigFloat import BigFloat
from data.message.DataMessageHandler import DataMessageHandler
from data.message.DataMessageProcessor import DataMessageProcessor
from utility.json_utility import as_data


class BinanceDataMessageProcessor(DataMessageProcessor):

    def __init__(self, message_handler: DataMessageHandler):
        self.message_handler = message_handler

    def process_message(self, message):
        symbol = as_data(message, 's')
        price = as_data(message, 'c')
        # todo: use transform rules (instrument + rate needs rules)
        print(f'transforming instrument:[{symbol}] price:[{price}]')
        exchange_rate = ExchangeRate('BTC', 'USDT', BigFloat(price))
        self.message_handler.handle_message(exchange_rate)
