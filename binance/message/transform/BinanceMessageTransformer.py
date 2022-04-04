from typing import Optional

from cache.provider.RedisCacheProvider import RedisCacheProvider
from core.exchange.ExchangeRate import ExchangeRate
from core.number.BigFloat import BigFloat
from utility.json_utility import as_data


class BinanceMessageTransformer:

    def __init__(self, options):
        self.transform_rules = self.load_transform_rules(options)

    def load_transform_rules(self, options):
        transform_rules_server_url = options['MESSAGE_TRANSFORM_RULES_URL']
        cache_provider = self.init_cache_provider(transform_rules_server_url)
        transform_rules = cache_provider.fetch(options['MESSAGE_TRANSFORM_RULES_KEY'], as_type=dict)
        return dict(self.unpack_transform_rules(transform_rules))

    @staticmethod
    def init_cache_provider(transform_rules_server_url):
        (server_address, server_port) = tuple(transform_rules_server_url.split(':'))
        options = {
            'REDIS_SERVER_ADDRESS': server_address,
            'REDIS_SERVER_PORT': int(server_port)
        }
        return RedisCacheProvider(options)

    @staticmethod
    def unpack_transform_rules(transform_rules):
        for transform_rule in transform_rules:
            yield as_data(transform_rule, 'instrument'), {'transform': as_data(transform_rule, 'transform'), 'ignore': as_data(transform_rule, 'ignore', False)}

    # todo: think about invert rule (return > 1)
    def transform(self, symbol, price) -> Optional[ExchangeRate]:
        if symbol in self.transform_rules:
            transform_rule = self.transform_rules[symbol]
            return self.transform_to_exchange_rate(transform_rule, price)
            # todo: invert (create another?)
        return None

    def transform_to_exchange_rate(self, transform_rule, price):
        if transform_rule['ignore'] is True:
            return None
        (currency, invert) = self.extract_transform_constituents(transform_rule['transform'])
        (from_currency, to_currency) = tuple(currency.split('/'))
        return ExchangeRate(from_currency, to_currency, BigFloat(price))

    @staticmethod
    def extract_transform_constituents(transform):
        return as_data(transform, 'currency'), as_data(transform, 'invert', False)

