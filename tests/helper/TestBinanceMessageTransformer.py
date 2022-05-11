from binance.message.exchange.rates.transform.BinanceExchangeMessageTransformer import BinanceExchangeMessageTransformer


class TestBinanceMessageTransformer(BinanceExchangeMessageTransformer):

    def __init__(self, transformations):
        self.transformations = dict(self.unpack_transformations(transformations))
