from src.infra.database.base_repository import BaseRepository


class CryptoRepository:

    def __init__(self):
        self.database = BaseRepository()


    def save(
        self,
        name: str,
        symbol: str,
        currency: str,
        current_price: float,
        market_cap: float,
        total_volume: float,
        price_change_percentage_24h: float,
        last_updated
    ):
        query = """
            INSERT INTO crypto_market_history (
                name,
                symbol,
                currency,
                current_price,
                market_cap,
                total_volume,
                price_change_percentage_24h,
                last_updated
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        params = (
            name,
            symbol,
            currency,
            current_price,
            market_cap,
            total_volume,
            price_change_percentage_24h,
            last_updated
        )

        self.database.insert(query, params)

        print("Cripto salva com sucesso!")