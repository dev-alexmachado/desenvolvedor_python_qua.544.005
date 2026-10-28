# importa o módulo
from modulo import eq_1o_grau, limpar


def main():
    limpar()
    a = float(input("Informe o valor de 'a': ").replace(",","."))
    b = float(input("Informe o valor de 'b': ").replace(",","."))
    x = eq_1o_grau(a,b)
    limpar()
    print(f"O valor de x é {x}.")


if __name__ == "__main__":
    main()