# dicionário
usuario = {
    'nome': "Fulano de Tal",
    'idade': 18,
    'email': "fulano@gmail.com"
}

# usuário informa o nome da nova chave
nova_chave = input("Informe o nome da nova chave: ").strip().lower()
# usuario informa o valor da nova chave
usuario[nova_chave] = input("Informe o valor da nova chave: ").strip()

# exibe o dicionário
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}.")