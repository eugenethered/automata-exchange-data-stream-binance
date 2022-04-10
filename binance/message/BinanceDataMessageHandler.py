from cache.holder.RedisCacheHolder import RedisCacheHolder
from core.exchange.ExchangeRate import ExchangeRate
from data.message.DataMessageHandler import DataMessageHandler


class BinanceDataMessageHandler(DataMessageHandler):

    def __init__(self, options):
        self.timeseries_key = options['TIMESERIES_KEY']
        self.cache = RedisCacheHolder()

    def handle_message(self, exchange_rate: ExchangeRate, event_time):
        print(f'Event time:{event_time} Binance exchange rate:{exchange_rate}')
        timeseries_key = self.exchange_rate_timeseries_key(exchange_rate)
        self.cache.create_timeseries(timeseries_key, 'rate')
        self.cache.add_to_timeseries(timeseries_key, event_time, exchange_rate.rate)

    def exchange_rate_timeseries_key(self, exchange_rate: ExchangeRate):
        currency_pairs = f'{exchange_rate.currency}/{exchange_rate.to_currency}'
        return self.timeseries_key.format(currency_pairs)
