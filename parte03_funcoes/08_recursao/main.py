# biblioteca
import os


# função limpa tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# função recursiva
def fatorial(n):
    return 1 if n == 1 else n*fatorial(n-1)

# função principal
def main():
    limpar()
    try:
        n = int(input("Informe um número inteiro: "))
        limpar()
        print(f"Fatorial de {n}! é {fatorial(n)}.")
    except Exception as e:
        print(f"Não foi possível calcular o fatorial. {e}.")


if __name__ == "__main__":
    main()