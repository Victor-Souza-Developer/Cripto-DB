from src.infra.database.conections import get_connection


class BaseRepository:

    def execute(self, query: str, params: tuple = None):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(query, params)
        connection.commit()

        cursor.close()
        connection.close()

    def insert(self, query: str, params: tuple):
        self.execute(query, params)

    def update(self, query: str, params: tuple):
        self.execute(query, params)

    def delete(self, query: str, params: tuple):
        self.execute(query, params)