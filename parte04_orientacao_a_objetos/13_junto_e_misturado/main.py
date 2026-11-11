import os
import random

from model import ContaCorrente,ContaPoupanca,Pessoa


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def operacoes(agencia,conta,usuario):
    if conta == "1":
        conta = ContaCorrente(
            agencia=agencia,
            n_conta=f"{random.randint(10000,99999)}-1",
            tipo_conta="Conta Corrente",
            saldo=0.0,
            titular=usuario,
            taxa=0.01
        )
    else:
        conta = ContaPoupanca(
            agencia=agencia,
            n_conta=f"{random.randint(10000,99999)}-2",
            tipo_conta="Conta Poupança",
            saldo=0.0,
            titular=usuario,
            juros=0.1
        )
    while True:
        print("0 - Sair do programa")
        print("1 - Consultar dados da conta")
        print("2 - Depositar dinheiro")
        print("3 - Sacar dinheiro")
        opcao = input("Operação desejada: ").strip()
        limpar()
        match opcao:
            case "0":
                break
            case "1":
                conta.consultar()
                continue
            case "2":
                valor = float(input("Informe o valor do depósito: R$ ").replace(",","."))
                saldo = conta.depositar(valor)
                limpar()
                print(f"Depósito efetuado com sucesso. Saldo atual: R$ {saldo:.2f}")
                continue
            case "3":
                valor = float(input("Informe o valor do saque: R$ ").replace(",","."))
                if valor < conta.saldo:
                    saldo = conta.sacar(valor)
                    limpar()
                    print(f"Saque efetuado com sucesso. Saldo atual: R$ {saldo:.2f}")
                else:
                    print("Saque não permitido.")
                continue
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