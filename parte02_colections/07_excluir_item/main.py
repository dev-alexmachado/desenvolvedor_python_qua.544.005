# lista
frutas = [
    'Maçã',
    'Pera',
    'Maracujá',
    'Morango',
    'Manga',
    'Melancia',
    'Goiaba'
]

while True:
    # exibe lista
    for n, fruta in enumerate(frutas):
        print(f"Índice {n}: {fruta}")

    # menu
    print("1 - Excluir fruta")
    print("2 - Encerrar programa")
    opcao = input("Opção desejada: ").strip()

    # verifica opção
    match opcao:
        case "1":
            indice = int(input("Informe o índice a ser excluído: "))
            del(frutas[indice]) # exclui indice selecionado
            print("Fruta excluída com sucesso!")
            continue
        case "2":
            break
        case _:
            print("Opção inválida.")
            continue
