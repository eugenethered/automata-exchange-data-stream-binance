from binance.message.exchange.rates.transform.BinanceExchangeMessageTransformer import BinanceExchangeMessageTransformer


class TestBinanceMessageTransformer(BinanceExchangeMessageTransformer):

    def __init__(self, transformations):
        self.transform_rules = dict(self.unpack_transformations(transformations))
