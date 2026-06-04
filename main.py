import time
from src.main.caller import Caller

def main():

    caller = Caller()
    while True:
        print("Iniciando coleta...")
        caller.run()
        print("Próxima coleta em 30 minutos...")
        time.sleep(86400)

if __name__ == "__main__":
    main()