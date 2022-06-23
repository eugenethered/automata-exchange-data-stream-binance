from cache.holder.RedisCacheHolder import RedisCacheHolder
from cache.provider.RedisCacheProviderWithHash import RedisCacheProviderWithHash
from exchangetransformrepo.ExchangeTransform import ExchangeTransform
from exchangetransformrepo.repository.ExchangeTransformRepository import ExchangeTransformRepository


class TransformationStoreHandler:

    def __init__(self, options):
        self.cache = RedisCacheHolder(options, held_type=RedisCacheProviderWithHash)
        self.repository = ExchangeTransformRepository(options)

    @staticmethod
    def obtain_transformations():
        return [
            ExchangeTransform(instrument='BTCUSDT', transform={
                'instruments': 'BTC/USDT'
            }),
            ExchangeTransform(instrument='BNBUSDT', transform={
                'instruments': 'BNB/USDT'
            }),
            ExchangeTransform(instrument='ADAUPUSDT', ignore=True)
        ]

    def store_transformations(self):
        transformations = self.obtain_transformations()
        self.repository.store_all(transformations)
        print(f'Stored [{len(transformations)}] transformations')
