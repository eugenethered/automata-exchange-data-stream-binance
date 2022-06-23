from simulation.transform.TransformationStoreHandler import TransformationStoreHandler

if __name__ == '__main__':

    options = {
        'REDIS_SERVER_ADDRESS': '192.168.1.90',
        'REDIS_SERVER_PORT': 6379,
        'EXCHANGE_TRANSFORMATIONS_KEY': 'binance:transformation:mv:exchange'
    }

    transformations_handler = TransformationStoreHandler(options)
    transformations_handler.store_transformations()
