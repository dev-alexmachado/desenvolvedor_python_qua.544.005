# dicionário
usuario = {
    'nome': "Alex Machado",
    'idade': 41,
    'email': "alex@gmail.com",
    'telefone': "(61) 98765-4321",
    'endereço': "Campo da Esperança"
}

# exibe a lista original
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")

# informa a chave a ser deletada
chave_escolhida = input("Informe a chave a excluir: ").strip().lower()

# deleta a chave
del usuario[chave_escolhida]

# re-exibe o novo dicionário
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")