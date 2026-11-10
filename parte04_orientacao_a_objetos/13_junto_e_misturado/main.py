import os
import random

from model import ContaCorrente,ContaPoupanca,Pessoa


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# TODO: terminar função operacoes()
def operacoes(agencia,conta,usuario):
    if conta == "1":
        conta = ContaCorrente(
            agencia=agencia,
            n_conta=f"{random.randint(10000,99999)}-1",
            saldo=0.0,
            titular=usuario,
            taxa=0.01
        )
    else:
        conta = ContaPoupanca(
            agencia=agencia,
            n_conta=f"{random.randint(10000,99999)}-2",
            saldo=0.0,
            titular=usuario,
            juros=0.01
        )
    while True:
        print("0 - Sair do programa")
        print("1 - Consultar dados da conta")
        print("2 - Depositar dinheiro")
        print("3 - Sacar dinheiro")
        opcao = input("Operação desejada: ").strip()
        match opcao:
            case "0":
                break
            case "1":
                # TODO
                pass
            case "2":
                # TODO
                pass
            case "3":
                # TODO
                pass
            case _:
                print("Opção inválida.")
                continue

def main():
    usuario = Pessoa(nome="",cpf="")

    limpar()
    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf = input("Informe o CPF: ").strip()
    limpar()
    print("1 - Criar Conta Corrente")
    print("2 - Criar Conta Poupança")
    conta = input("Informe o tipo de conta que deseja criar: ").strip()
    limpar()
    if conta == "1" or conta == "2":
        operacoes("1234-1",conta,usuario)
    else:
        print("Tipo de conta inválido.")


if __name__ == "__main__":
    main()