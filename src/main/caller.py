from src.infra.clients.coingecko_client import CoinGeckoClient
from src.infra.database.crypto_repository import CryptoRepository

class Caller:

    def __init__(self):
        self.client = CoinGeckoClient()
        self.repository = CryptoRepository()


    def run(self):
        market_data = self.client.get_market_data()

        for item in market_data:

            self.repository.save(
                name=item["name"],
                symbol=item["symbol"],
                currency="USD",
                current_price=item["current_price"],
                market_cap=item["market_cap"],
                total_volume=item["total_volume"],
                price_change_percentage_24h=item["price_change_percentage_24h"],
                last_updated=item["last_updated"]
            )