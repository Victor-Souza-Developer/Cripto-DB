from src.infra.database.conections import get_connection


def main():
    connection = get_connection()

    print("Conectado com sucesso ao PostgreSQL")

    connection.close()


if __name__ == "__main__":
    main()