from binance.message.exchange.rates.transform.BinanceExchangeMessageTransformer import BinanceExchangeMessageTransformer


class TestBinanceMessageTransformer(BinanceExchangeMessageTransformer):

    def __init__(self, transform_rules):
        self.transform_rules = dict(self.unpack_transform_rules(transform_rules))
