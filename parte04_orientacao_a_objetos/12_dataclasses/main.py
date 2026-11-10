import os

from model import Pessoa


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = Pessoa(nome="",cpf="",email="",idade=0,altura=0.0)

    limpar()
    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.email = input("Informe o e-mail: ").strip().lower()
    usuario.idade = int(input("Informe a idade: "))
    usuario.altura = float(input("Informe a altura: ").replace(",","."))

    limpar()
    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
    print(f"E-mail: {usuario.email}")
    print(f"Idade: {usuario.idade}")
    print(f"Altura: {usuario.altura}")


if __name__ == "__main__":
    main()