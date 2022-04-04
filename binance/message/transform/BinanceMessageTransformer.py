from cache.provider.RedisCacheProvider import RedisCacheProvider


class BinanceMessageTransformer:

    def __init__(self, options):
        transform_rules = self.load_transform_rules(options)
        print(f'Transform rules! {transform_rules}')

    def load_transform_rules(self, options):
        transform_rules_server_url = options['MESSAGE_TRANSFORM_RULES_URL']
        cache_provider = self.init_cache_provider(transform_rules_server_url)
        return cache_provider.fetch(options['MESSAGE_TRANSFORM_RULES_KEY'], as_type=dict)

    @staticmethod
    def init_cache_provider(transform_rules_server_url):
        (server_address, server_port) = tuple(transform_rules_server_url.split(':'))
        options = {
            'REDIS_SERVER_ADDRESS': server_address,
            'REDIS_SERVER_PORT': int(server_port)
        }
        return RedisCacheProvider(options)
