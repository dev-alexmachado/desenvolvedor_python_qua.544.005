# bibliotecas
import os


tarefas = [] # lista vazia


os.system("cls" if os.name == "nt" else "clear") # limpa terminal


# loop
while True:
    # menu
    print("1 - Inserir nova tarefa na lista")
    print("2 - Finalizar e exibir lista")
    opcao = input("Opção desejada: ").strip() # informa opção desejada

    # verifica a opção informada
    match opcao:
        case "1":
            nova_tarefa = input("Informe a nova tarefa: ") # informa novo item
            tarefas.append(nova_tarefa) # insere item na lista
            continue # retorna para o início do loop
        case "2":
            os.system("cls" if os.name == "nt" else "clear")

            # exibe a lista
            for n, tarefa in enumerate(tarefas, start=1):
                print(f"{n}ª tarefa: {tarefa}")
            break # encerra o loop
        case _:
            print("Opção inválida.")