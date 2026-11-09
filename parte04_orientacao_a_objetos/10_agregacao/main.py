import os

from model import Empresa, Departamento


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    departamento = Departamento(nome="")
    empresa = Empresa(razao_social="",nome_fantasia="",cnpj="",departamento=departamento)

    limpar()
    print("Defina os dados da empresa:")
    empresa.razao_social = input("Informe a razão social: ").strip()
    empresa.nome_fantasia = input("Informe o nome: ").strip()
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.departamento.nome = input("Informe o departamento em que trabalha: ").strip()

    limpar()
    print(empresa.detalhes())


if __name__ == "__main__":
    main()