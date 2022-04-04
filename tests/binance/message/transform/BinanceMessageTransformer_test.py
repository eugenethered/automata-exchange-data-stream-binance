import unittest

from core.number.BigFloat import BigFloat

from binance.message.transform.BinanceMessageTransformer import BinanceMessageTransformer


class BinanceMessageTransformerTestCase(unittest.TestCase):

    def test_should_transform_symbol_price_to_exchange_rate(self):
        transform_rules = [{
            'instrument': 'BNBUSDT',
            'transform': {
                'currency': 'BNB/USDT'
            }
        }]
        transformer = TestBinanceMessageTransformer(transform_rules)
        exchange_rate = transformer.transform('BNBUSDT', '445.20000000')
        self.assertEqual('BNB', exchange_rate.currency)
        self.assertEqual('USDT', exchange_rate.to_currency)
        self.assertEqual(BigFloat('445.20000000'), exchange_rate.rate)

    def test_should_not_transform_symbol_price_to_exchange_rate_when_rule_for_symbol_not_present(self):
        transform_rules = []
        transformer = TestBinanceMessageTransformer(transform_rules)
        exchange_rate = transformer.transform('BNBETH', '0.1274')
        self.assertEqual(None, exchange_rate)

    def test_should_not_transform_symbol_when_transform_rule_is_explicitly_ignored(self):
        transform_rules = [{
            'instrument': 'BNBZWL',
            'ignore': True
        }]
        transformer = TestBinanceMessageTransformer(transform_rules)
        exchange_rate = transformer.transform('BNBZWL', '1000000000.00')
        self.assertEqual(None, exchange_rate)


class TestBinanceMessageTransformer(BinanceMessageTransformer):

    def __init__(self, transform_rules):
        self.transform_rules = dict(self.unpack_transform_rules(transform_rules))


if __name__ == '__main__':
    unittest.main()
