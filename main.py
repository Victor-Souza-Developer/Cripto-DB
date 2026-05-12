import time
from src.main.caller import Caller

def main():

    caller = Caller()
    while True:
        print("Iniciando coleta...")
        caller.run()
        print("Próxima coleta em 10 minutos...")
        time.sleep(600)

if __name__ == "__main__":
    main()