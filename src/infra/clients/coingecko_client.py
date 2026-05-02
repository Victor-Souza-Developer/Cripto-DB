import requests


class CoinGeckoClient:

    BASE_URL = "https://api.coingecko.com/api/v3"


    def get_market_data(self):
        endpoint = "/coins/markets"

        params = {
            "vs_currency": "usd",
            "ids": "bitcoin,ethereum,ripple,solana,cardano"
        }

        response = requests.get(
            url=f"{self.BASE_URL}{endpoint}",
            params=params
        )

        return response.json()