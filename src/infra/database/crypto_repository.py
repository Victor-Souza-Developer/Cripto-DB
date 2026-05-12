from src.infra.database.conections import get_connection


class CryptoRepository:

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
        connection = get_connection()
        cursor = connection.cursor()

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

        cursor.execute(query, params)

        connection.commit()

        cursor.close()
        connection.close()

        print("Cripto salva com sucesso!")