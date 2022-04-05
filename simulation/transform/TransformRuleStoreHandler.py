from cache.holder.RedisCacheHolder import RedisCacheHolder


class TransformRuleStoreHandler:

    def __init__(self, options):
        self.cache = RedisCacheHolder(options)

    @staticmethod
    def obtain_transformation_rules():
        return [
            {
                'instrument': 'BTCUSDT',
                'transform': {
                    'currency': 'BTC/USDT'
                }
            },
            {
                'instrument': 'BNBUSDT',
                'transform': {
                    'currency': 'BNB/USDT'
                }
            }
        ]

    def store_transformation_rules(self, key):
        transformation_rules = self.obtain_transformation_rules()
        self.cache.store(key, transformation_rules)
        print(f'Stored [{len(transformation_rules)}] transformation rules')
