from cache.holder.RedisCacheHolder import RedisCacheHolder


class TransformRuleStoreHandler:

    def __init__(self, options):
        self.cache = RedisCacheHolder(options)

    @staticmethod
    def obtain_transformation_rules():
        # todo: when 'invert' should add another exchange rate with inverted rate
        return [
            {
                'instrument': 'BTCUSDT',
                'transform': {
                    'instruments': 'BTC/USDT'
                }
            },
            {
                'instrument': 'BNBUSDT',
                'transform': {
                    'instruments': 'BNB/USDT',
                    'invert': True
                }
            }
        ]

    def store_transformation_rules(self, key):
        transformation_rules = self.obtain_transformation_rules()
        self.cache.store(key, transformation_rules)
        print(f'Stored [{len(transformation_rules)}] transformation rules')
