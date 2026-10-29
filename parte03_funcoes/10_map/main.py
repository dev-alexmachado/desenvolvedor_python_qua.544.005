import os


limpar = lambda: os.system("cls" if os.name == "nt" else "clear")
pg = lambda x: x*2

def main():
    # lista original
    numeros = [1,2,3,4,5,6,7,8,9]

    limpar()
    print(numeros)

    numeros_pg = list(map(pg, numeros))

    # exibe a nova lista com a pg aplicada
    print(f"Nova lista com pg: {numeros_pg}")


if __name__ == "__main__":
    main()