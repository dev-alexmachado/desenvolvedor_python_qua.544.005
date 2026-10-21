# tupla
dias_da_semana = (
    "Domingo",
    "Segunda-Feira",
    "Terça-Feira",
    "Quarta-Feira",
    "Quinta-Feira",
    "Sexta-Feira",
    "Sábado"
)

# exibe a tupla
for dia in dias_da_semana:
    print(dia)

# NOTE: se tentar alterar a tupla, o programa dá erro. Exemplo
try:
    dias_da_semana.sort()
    for dia in dias_da_semana:
        print(dia)
except Exception as e:
    print(f"Não foi possíve ordenar. {e}.")
finally:
    print("Programa encerrado.")