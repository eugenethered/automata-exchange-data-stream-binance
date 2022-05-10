from cache.holder.RedisCacheHolder import RedisCacheHolder


class TransformRuleStoreHandler:

    def __init__(self, options):
        self.cache = RedisCacheHolder(options)

    @staticmethod
    def obtain_transformations():
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
                    'instruments': 'BNB/USDT'
                }
            }
        ]

    def store_transformations(self, key):
        transformations = self.obtain_transformations()
        self.cache.store(key, transformations)
        print(f'Stored [{len(transformations)}] transformations')
