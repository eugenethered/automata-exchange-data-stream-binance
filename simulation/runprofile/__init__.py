from cache.holder.RedisCacheHolder import RedisCacheHolder
from processrepo.ProcessRunProfile import ProcessRunProfile, RunProfile
from processrepo.repository.ProcessRunProfileRepository import ProcessRunProfileRepository

if __name__ == '__main__':

    options = {
        'REDIS_SERVER_ADDRESS': '192.168.1.90',
        'REDIS_SERVER_PORT': 6379,
        'PROCESS_RUN_PROFILE_KEY': '{}:process:run-profile:{}'
    }

    RedisCacheHolder(options)

    process_run_profile = ProcessRunProfile('binance', 'exchange-data-stream', RunProfile.ASAP)

    repository = ProcessRunProfileRepository(options)
    repository.store(process_run_profile)

    print('Process Run Profile stored!')
