# biblioteca
import os

# declaração de funções
def boas_vindas(nome):
    print(f"{nome}, seja bem-vindo!")

def limpar():
    os.system("cls" if os.name == "nt" else "clear")


# algoritmo principal
limpar()
nome = input("Informe seu nome: ").strip().title()
boas_vindas(nome)