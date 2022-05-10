import unittest

from core.number.BigFloat import BigFloat
from exchangetransformrepo.ExchangeTransform import ExchangeTransform

from tests.helper.TestBinanceMessageTransformer import TestBinanceMessageTransformer


class BinanceMessageTransformerTestCase(unittest.TestCase):

    def test_should_transform_symbol_price_to_exchange_rate(self):
        exchange_transform = [
            ExchangeTransform('BNBUSDT', {
                'instruments': 'BNB/USDT'
            })
        ]
        transformer = TestBinanceMessageTransformer(exchange_transform)
        exchange_rate = transformer.transform('BNBUSDT', '445.20000000')
        self.assertEqual('BNB', exchange_rate.instrument)
        self.assertEqual('USDT', exchange_rate.to_instrument)
        self.assertEqual(BigFloat('445.20000000'), exchange_rate.rate)

    def test_should_not_transform_symbol_price_to_exchange_rate_when_rule_for_symbol_not_present(self):
        exchange_transform = []
        transformer = TestBinanceMessageTransformer(exchange_transform)
        exchange_rate = transformer.transform('BNBETH', '0.1274')
        self.assertEqual(None, exchange_rate)

    def test_should_not_transform_symbol_when_transform_rule_is_explicitly_ignored(self):
        exchange_transform = ExchangeTransform('BNBZWL')
        exchange_transform.ignore = True
        exchange_transformations = [exchange_transform]
        transformer = TestBinanceMessageTransformer(exchange_transformations)
        exchange_rate = transformer.transform('BNBZWL', '1000000000.00')
        self.assertEqual(None, exchange_rate)


if __name__ == '__main__':
    unittest.main()
