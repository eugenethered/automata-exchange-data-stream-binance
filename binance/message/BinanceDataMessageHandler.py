from core.exchange.ExchangeRate import ExchangeRate
from data.message.DataMessageHandler import DataMessageHandler


class BinanceDataMessageHandler(DataMessageHandler):

    def handle_message(self, exchange_rate: ExchangeRate, event_time):
        print(f'Event time:{event_time} Binance exchange rate:{exchange_rate}')
        # todo: save these exchange rates
        # todo: check 1649185190231 against run-instance
