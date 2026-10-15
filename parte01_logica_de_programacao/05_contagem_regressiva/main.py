# importa as bibliotecas
import os
import time

# limpa o terminal
os.system("cls")

# entrada de dados
n = int(input("Informe um número inteiro: "))

# contador
while n >= 0:
    os.system("cls")
    print(f"{n}...")
    time.sleep(1)
    n -= 1
print("BOOM!!!!")