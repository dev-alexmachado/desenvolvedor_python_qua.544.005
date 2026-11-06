import os

from model import CarroVoador


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    carro_voador = CarroVoador(
        cambio=True,
        estepe=False,
        porta_malas=False,
        volante=True,
        retrovisor=True,
        buzina=True,
        escapamento=True,
        asa=True,
        turbina=True,
        aerofolio=True,
        cauda=True,
        manche=True,
        caixa_preta=True
    )

    limpar()
    print(f"Câmbio: {carro_voador.cambio}")
    print(f"Estepe: {carro_voador.estepe}")
    print(f"Porta Malas: {carro_voador.porta_malas}")
    print(f"Volante: {carro_voador.volante}")
    print(f"Retrovisor: {carro_voador.retrovisor}")
    print(f"Buzina: {carro_voador.buzina}")
    print(f"Escapamento: {carro_voador.escapamento}")
    print(f"Asa: {carro_voador.asa}")
    print(f"Turbina: {carro_voador.turbina}")
    print(f"Aerofólio: {carro_voador.aerofolio}")
    print(f"Cauda: {carro_voador.cauda}")
    print(f"Manche: {carro_voador.manche}")
    print(f"Caixa Preta: {carro_voador.caixa_preta}")


if __name__ == "__main__":
    main()