from model import Carro


def main():
    carro = Carro(fabricante="",modelo="",ano=0,cor="",potencia=600)

    print("Dados do carro que vai receber o motor:")
    carro.fabricante = input("Informe o fabricante: ").strip()
    carro.modelo = input("Informe o modelo: ").strip()
    carro.ano = int(input("Informe o ano: "))
    carro.cor = input("Informe a cor: ").strip()

    print(carro.exibir_detalhes())


if __name__ == "__main__":
    main()