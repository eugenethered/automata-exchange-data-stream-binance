from core.exchange.ExchangeRate import ExchangeRate
from data.message.DataMessageHandler import DataMessageHandler


class BinanceDataMessageHandler(DataMessageHandler):

    def handle_message(self, exchange_rate: ExchangeRate):
        print(f'Binance exchange rate -> {exchange_rate}')
        # todo: save these exchange rates
