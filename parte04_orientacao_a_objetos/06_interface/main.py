# bibliotecas
import os
import random

from model import Conta


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    # instancia a classe Conta
    cc = Conta(
        titular="",
        cpf="",
        agencia="1010-1",
        n_conta=f"{random.randint(10000,99999)}-1",
        saldo=0.0
    )

    # TODO: terminar dia 06/11/2026


if __name__ == "__main__":
    main()