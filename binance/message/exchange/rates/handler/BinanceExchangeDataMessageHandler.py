from core.exchange.ExchangeRate import ExchangeRate
from exchangerepo.repository.ExchangeRateRepository import ExchangeRateRepository


class BinanceExchangeDataMessageHandler:

    def __init__(self, repository: ExchangeRateRepository):
        self.repository = repository

    def handle_exchange_rate(self, exchange_rate: ExchangeRate, event_time):
        if exchange_rate is not None:
            self.repository.store(exchange_rate, event_time)