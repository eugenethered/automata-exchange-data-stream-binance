from simulation.transform.TransformRuleStoreHandler import TransformRuleStoreHandler

if __name__ == '__main__':

    options = {
        'REDIS_SERVER_ADDRESS': '192.168.1.90',
        'REDIS_SERVER_PORT': 6379
    }

    TRANSFORMATION_RULES_KEY = 'binance:message:transform-rules'

    rule_handler = TransformRuleStoreHandler(options)
    rule_handler.store_transformation_rules(TRANSFORMATION_RULES_KEY)
