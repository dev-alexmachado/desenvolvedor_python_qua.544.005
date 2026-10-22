# biblioteca
import os


# lista de usuários vazia
usuarios = []

# limpa terminal
os.system("cls" if os.name == "nt" else "clear")

# loop
while True:
    # menu
    print("1 - Cadastrar novo usuário")
    print("2 - Exibir lista de usuários")
    print("3 - Sair do programa")
    opcao = input("Opção desejada: ").strip()

    os.system("cls" if os.name == "nt" else "clear")

    # verifica opção escolhida
    match opcao:
        case "1":
            # cria novo dicionário
            usuario = {}

            # insere os dados no dicionário
            usuario['nome'] = input("Informe o nome: ").strip().title()
            usuario['idade'] = int(input("Informe a idade: "))
            usuario['email'] = input("Informe o e-mail: ").strip().lower()
            usuario['cpf'] = input("Informe o CPF: ").strip()

            # adiciona o usuário na lista
            usuarios.append(usuario)

            # mensagem de sucesso
            print(f"{usuario.get('nome')} cadastrado com sucesso!")
            continue
        case "2":
            # exibe a lista de usuários
            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")
                print(f"{'-'*40}")
            continue
        case "3":
            break
        case _:
            print("Opção inválida.")
            continue