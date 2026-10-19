# import a biblioteca
import os

# limpa terminal
os.system("cls" if os.name == "nt" else "clear")

# dados do usuário
nome = input("Informe seu nome: ").strip().title()
idade = int(input("Informe sua idade: "))
idade_minima = None

# loop
while True:
    # menu de filmes
    print(f"{'-'*20} CINE COBRA {'-'*20}")
    print("Sala 1 - A Roda Quadrada - Livre")
    print("Sala 2 - A Volta dos Que Não Foram - 12 anos")
    print("Sala 3 - As Tranças do Rei Careca - 14 anos")
    print("Sala 4 - Poeira em Alto Mar - 16 anos")
    print("Sala 5 - A Vingança do Peixe Frito - 18 anos")

    # usuário informa a sala do filme desejado
    sala = input("Sala desejada: ").strip()

    # atribui a idade mínima do filme
    match sala:
        case "1":
            idade_minima = 0
        case "2":
            idade_minima = 12
        case "3":
            idade_minima = 14
        case "4":
            idade_minima = 16
        case "5":
            idade_minima = 18
        case _:
            print("Sala inexistente.")
            idade_minima = idade + 1
    # verifica a idade
    if idade >= idade_minima:
        print(f"Ingresso impresso para {nome}")
        print("Tenha um bom filme!")
        break
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Ingresso negado para {nome}")
        print("Você não possui a idade mínima para ver o filme!")
        print("Por favor, escolha outro filme:")
        continue

# TODO: atividade 02
'''
Crie um programa em que o usuário informe uma única vez o nome e a idade, e em seguida, o programa exibe uma lista de 5 filmes do cinema e suas respectivas salas e classificações indicativas.
O usuário deverá escolher a sala do filme desejado. Se tiver a idade mínima, o programa imprime o ingresso e encerra. Senão, o programa impede a entrada do usuário e retorna a lista para que o mesmo possa escolher outro filme.
'''