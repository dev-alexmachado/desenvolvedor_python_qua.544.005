# bibliotecas
import os


# lista
nomes = ["Alex", "Charlotte", "Scarlet", "John", "Jason", "Michael", "Connor"]

os.system("cls" if os.name == "nt" else "clear")


# loop
while True:
    # exibe a lista original
    for n, nome in enumerate(nomes):
        print(f"Índice {n}: {nome}")
    # menu
    print("1 - Alterar item da lista")
    print("2 - Finalizar")
    opcao = input("Opção desejada: ").strip() # informa opção desejada

    # verifica a opção escolhida
    match opcao:
        case "1":
            # informa índice a ser alterado
            indice = int(input("Informe o índice a ser alterado: "))
            # informa novo valor
            nomes[indice] = input("Informe novo nome: ").strip().title()
            os.system("cls" if os.name == "nt" else "clear")
            print("Item da lista alterado com sucesso!")
            continue
        case "2":
            os.system("cls" if os.name == "nt" else "clear")
            # exibe a nova lista
            for n, nome in enumerate(nomes):
                print(f"Índice {n}: {nome}")
            break
        case _:
            print("Opção inválida")
            continue