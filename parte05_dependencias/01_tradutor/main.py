# importando a biblioteca instalada
from translate import Translator

# importa biblioteca os
import os


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def traduzir(texto):
    tradutor = Translator(to_lang="pt")
    return tradutor.translate(texto)

def main():
    limpar()
    texto = input("Informe o texto a ser traduzido: ")
    print(f"\nTexto traduzido:\n{traduzir(texto)}")


if __name__ == "__main__":
    main()