import os


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def peso_astro(massa, gravidade):
    return massa * gravidade