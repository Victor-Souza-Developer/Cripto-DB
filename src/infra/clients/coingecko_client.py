from src.utils.env import Env
import requests



class CoinGeckoClient:

    def __init__(self):
        self.BASE_URL = Env.BASE_URL


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