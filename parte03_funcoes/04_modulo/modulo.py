# bibliotecas
import os
import math


# funções
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def a_quad(b, h):
    return b*h

def a_circulo(r):
    return math.pi*(r**2)

def comprimento_circulo(r):
    return 2*math.pi*r