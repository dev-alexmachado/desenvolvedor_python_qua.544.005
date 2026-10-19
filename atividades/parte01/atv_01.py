# entrada de dados
nome = input("Informe seu nome: ").strip().title()
massa = float(input("Informe sua massa em kg: ").replace(",","."))
altura = float(input("Informe sua altura em metros: ").replace(",","."))

# calcula o imc
imc = massa/(altura**2)

# exibe o valor do imc
print(f"{nome}, seu IMC é {imc:.2f}!")

# informa o diagnóstico do usuário
if imc < 18.5:
    print("Você está com massa abaixo do normal.")
elif imc < 25:
    print("Você está com massa normal.")
elif imc < 30:
    print("Você está com massa acima do normal. ")
elif imc < 35:
    print("Você está obeso.")
elif imc < 40:
    print("Você está com obesidade nível II.")
else:
    print("Você est]á com obesidade mórbida.")

# atividade 01
'''
Crie um programa que receba o nome, a massa em kg e a altura em metros do usuário, calcule seu IMC (índice de massa corporal) e finalize informado o diagnóstico do usuário com base no valor do IMC (se está magro, gordo, no peso ideal...)
'''
# NOTE: ATENÇÃO!!!! DIVIRTAM-SE!!!!