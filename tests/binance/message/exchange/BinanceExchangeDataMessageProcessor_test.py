import unittest

from core.exchange.ExchangeRate import ExchangeRate
from core.number.BigFloat import BigFloat
from exchangetransformrepo.ExchangeTransform import ExchangeTransform

from binance.message.exchange.rates.BinanceExchangeDataMessageProcessor import BinanceExchangeDataMessageProcessor
from binance.message.exchange.rates.handler.BinanceExchangeDataMessageHandler import BinanceExchangeDataMessageHandler
from tests.helper.TestBinanceMessageTransformer import TestBinanceMessageTransformer


class BinanceDataMessageProcessorTestCase(unittest.TestCase):

    def test_should_extract_symbol_and_price_from_message(self):
        message = {
            'A': '0.04280400',
            'B': '0.03226400',
            'C': 1648913426946,
            'E': 1648913430060,
            'F': 4732465,
            'L': 4840067,
            'O': 1648827026946,
            'P': '-0.154',
            'Q': '0.04087000',
            'a': '46491.60000000',
            'b': '46491.59000000',
            'c': '46488.89000000',
            'e': '24hrTicker',
            'h': '95000.00000000',
            'l': '44477.76000000',
            'n': 107603,
            'o': '46560.65000000',
            'p': '-71.76000000',
            'q': '119188022.26977675',
            's': 'BTCUSDT',
            'v': '2564.68508800',
            'w': '46472.77080038',
            'x': '46560.65000000'
        }
        message_handler = TestMessageHandler()
        message_transformer = TestBinanceMessageTransformer(transformations=[
            ExchangeTransform('BTCUSDT', {
                'instruments': 'BTC/USDT'
            })
        ])
        message_processor = BinanceExchangeDataMessageProcessor(message_transformer, message_handler)
        message_processor.process_message(message)
        expected_exchange_rate = ExchangeRate('BTC', 'USDT', BigFloat('46488.89000000'))
        self.assertEqual(expected_exchange_rate, message_handler.exchange_rate)


class TestMessageHandler(BinanceExchangeDataMessageHandler):

    def __init__(self):
        self.exchange_rate = None

    def handle_exchange_rate(self, exchange_rate, event_time):
        self.exchange_rate = exchange_rate


if __name__ == '__main__':
    unittest.main()
