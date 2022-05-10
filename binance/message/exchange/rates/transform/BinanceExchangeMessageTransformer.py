import logging
from typing import Optional, List

from config.report.holder.ConfigReporterHolder import ConfigReporterHolder
from core.exchange.ExchangeRate import ExchangeRate
from core.market.Market import Market
from core.missing.Context import Context
from core.number.BigFloat import BigFloat
from exchangetransformrepo.ExchangeTransform import ExchangeTransform
from exchangetransformrepo.repository.ExchangeTransformRepository import ExchangeTransformRepository
from missingrepo.Missing import Missing
from utility.json_utility import as_data


class BinanceExchangeMessageTransformer:

    def __init__(self, repository: ExchangeTransformRepository):
        self.repository = repository
        self.config_reporter = ConfigReporterHolder()
        self.transform_rules = self.load_transform_rules()

    def load_transform_rules(self):
        exchange_transformations = self.repository.retrieve()
        return dict(self.unpack_transform_rules(exchange_transformations))

    @staticmethod
    def unpack_transform_rules(exchange_transformations: List[ExchangeTransform]):
        for exchange_transform in exchange_transformations:
            yield exchange_transform.instrument, exchange_transform

    # todo: think about invert rule (return > 1)
    def transform(self, symbol, price) -> Optional[ExchangeRate]:
        if symbol in self.transform_rules:
            logging.debug(f'Transformation Rule being applied to symbol:{symbol} with price:{price}')
            exchange_transformation = self.transform_rules[symbol]
            return self.transform_to_exchange_rate(exchange_transformation, price)
            # todo: invert (create another?)
        else:
            missing = Missing(symbol, Context.EXCHANGE, Market.BINANCE, f'Missing instrument:[{symbol}] with price:[{price}]')
            self.config_reporter.report_missing(missing)
            logging.warning(f'No Transformation Rule for symbol:{symbol} with price:{price}')
            return None

    def transform_to_exchange_rate(self, exchange_transformation, price):
        if exchange_transformation.ignore is True:
            return None
        (instruments, invert) = self.extract_transform_constituents(exchange_transformation.transform)
        (instrument, to_instrument) = tuple(instruments.split('/'))
        return ExchangeRate(instrument, to_instrument, BigFloat(price))

    @staticmethod
    def extract_transform_constituents(transform):
        return as_data(transform, 'instruments'), as_data(transform, 'invert', False)

