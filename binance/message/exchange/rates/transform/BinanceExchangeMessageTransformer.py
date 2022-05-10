import logging
from typing import Optional

from cache.holder.RedisCacheHolder import RedisCacheHolder
from config.report.holder.ConfigReporterHolder import ConfigReporterHolder
from core.exchange.ExchangeRate import ExchangeRate
from core.market.Market import Market
from core.missing.Context import Context
from core.number.BigFloat import BigFloat
from missingrepo.Missing import Missing
from utility.json_utility import as_data


class BinanceExchangeMessageTransformer:

    def __init__(self, options):
        self.config_reporter = ConfigReporterHolder()
        self.transform_rules = self.load_transform_rules(options)

    def load_transform_rules(self, options):
        cache = RedisCacheHolder()
        transform_rules = cache.fetch(options['EXCHANGE_TRANSFORMATION_RULES_KEY'], as_type=dict)
        return dict(self.unpack_transform_rules(transform_rules))

    @staticmethod
    def unpack_transform_rules(transform_rules):
        for transform_rule in transform_rules:
            yield as_data(transform_rule, 'instrument'), {'transform': as_data(transform_rule, 'transform'), 'ignore': as_data(transform_rule, 'ignore', False)}

    # todo: think about invert rule (return > 1)
    def transform(self, symbol, price) -> Optional[ExchangeRate]:
        if symbol in self.transform_rules:
            logging.debug(f'Transformation Rule being applied to symbol:{symbol} with price:{price}')
            transform_rule = self.transform_rules[symbol]
            return self.transform_to_exchange_rate(transform_rule, price)
            # todo: invert (create another?)
        else:
            missing = Missing(symbol, Context.EXCHANGE, Market.BINANCE, f'Missing instrument:[{symbol}] with price:[{price}]')
            self.config_reporter.report_missing(missing)
            logging.warning(f'No Transformation Rule for symbol:{symbol} with price:{price}')
            return None

    def transform_to_exchange_rate(self, transform_rule, price):
        if transform_rule['ignore'] is True:
            return None
        (instruments, invert) = self.extract_transform_constituents(transform_rule['transform'])
        (instrument, to_instrument) = tuple(instruments.split('/'))
        return ExchangeRate(instrument, to_instrument, BigFloat(price))

    @staticmethod
    def extract_transform_constituents(transform):
        return as_data(transform, 'instruments'), as_data(transform, 'invert', False)

