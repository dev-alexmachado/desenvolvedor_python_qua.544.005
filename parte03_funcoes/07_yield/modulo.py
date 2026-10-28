# bibliotecas
import math
import os


# funções
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def eq_2o_grau(a,b,c):
    delta = (b**2)-(4*a*c)
    if delta > 0:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        yield x1
        yield x2
    elif delta == 0:
        x = -b/(2*a)
        yield x
    else:
        yield "Não existem raízes reais."