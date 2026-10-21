# biblioteca
import os

# dicionário
usuario = {
    'nome': "Thomas Anderson",
    'idade': 40,
    'email': "mranderson@gmail.com",
    'telefone': "(61) 96666-6666"
}

# limpa terminal
os.system("cls" if os.name == "nt" else "clear")

# loop
while True:
    # exibe o dicionário
    for chave, valor in usuario.items():
        print(f"{chave}: {valor}")

    # informa o nome da chave
    chave_escolhida = input("Informe o nome da chave que deseja alterar ou Enter para encerrar: ").strip().lower()
    # verifica se a chave é válida
    if chave_escolhida:
        # informa o novo valor
        usuario[chave_escolhida] = input("Informe o novo valor: ").strip()
        continue
    else:
        break