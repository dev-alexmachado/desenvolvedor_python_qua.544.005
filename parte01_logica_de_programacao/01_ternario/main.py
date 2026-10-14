# declaração de variáveis
nome = input("Informe seu nome: ").strip().title()
idade = int(input("Informe sua idade: "))

# operador ternário
print(f"{nome} {'é maior de idade' if idade >=18 else 'é menor de idade'}.")