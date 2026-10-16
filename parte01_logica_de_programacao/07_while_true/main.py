# importa biblioteca
import os

# limpa a tela
os.system("cls" if os.name == "nt" else "clear")

# loop
while True:
    aluno = input("Informe o nome do aluno: ").strip().title()

    try:
        nota = float(input("Informe a nota de 0 a 10: ").replace(',','.'))

        if nota >= 0 and nota <= 10:
            if nota >= 7:
                print(f"{aluno} está aprovado.")
            elif nota >= 5:
                print(f"{aluno} está de recuperação.")
            else:
                print(f"{aluno} está reprovado.")
        else:
            print("Nota inválida.")
    except Exception as e:
        print(f"Não foi possível calcular a média. {e}.")
    continuar = input("Deseja inserir outra nota? 'sim' para prosseguir. Qualquer outro valor para encerrar:").strip().lower()

    if continuar == "sim":
        os.system("cls" if os.name == "nt" else "clear")
        continue
    else:
        break