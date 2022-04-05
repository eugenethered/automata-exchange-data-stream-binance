from binance.message.transform.BinanceMessageTransformer import BinanceMessageTransformer


class TestBinanceMessageTransformer(BinanceMessageTransformer):

    def __init__(self, transform_rules):
        self.transform_rules = dict(self.unpack_transform_rules(transform_rules))
