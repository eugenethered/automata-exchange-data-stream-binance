import logging

from cache.holder.RedisCacheHolder import RedisCacheHolder
from cache.provider.RedisCacheProviderWithHash import RedisCacheProviderWithHash
from config.report.holder.ConfigReporterHolder import ConfigReporterHolder
from core.environment.EnvironmentVariables import EnvironmentVariables
from logger.ConfigureLogger import ConfigureLogger
from timeseries.holder.InfluxDBHolder import InfluxDBHolder

from binance.BinanceExchangeDataStream import BinanceExchangeDataStream


def start():
    ConfigureLogger()

    environment_variables = EnvironmentVariables()

    log = logging.getLogger('Binance Exchange Data Stream')
    log.info(f'Starting with URL {environment_variables.url()}')

    RedisCacheHolder(environment_variables.options, held_type=RedisCacheProviderWithHash)

    InfluxDBHolder(environment_variables.options)

    ConfigReporterHolder(environment_variables.options)

    data_stream = BinanceExchangeDataStream(environment_variables.url(), environment_variables.options)
    data_stream.receive_data()


if __name__ == '__main__':
    start()
