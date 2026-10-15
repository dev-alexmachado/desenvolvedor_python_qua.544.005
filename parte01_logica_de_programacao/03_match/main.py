# declaração de variáveis
x = float(input("Informe um número: ").replace(",","."))
y = float(input("Informe outro número: ").replace(",","."))

# menu
print(f"{'-'*20} Escolha uma operação {'-'*20}")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operador = input("Operação desejada: ").strip()

# match...case
match operador:
    case "1":
        print(f"Resultado da soma: {x+y}")
    case "2":
        print(f"Resultado da subtração: {x-y}")
    case "3":
        print(f"Resultado da multiplicação: {x*y}")
    case "4":
        print(f"Resultado da divisão: {x/y}")
    case _: # default
        print("Operação inválida.")