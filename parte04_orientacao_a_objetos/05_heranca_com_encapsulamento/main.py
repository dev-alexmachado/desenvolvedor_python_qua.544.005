import os

from model import PessoaFisica,PessoaJuridica


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    # instancia as classes
    usuario = PessoaFisica(nome="",cpf="",email="",telefone="")
    empresa = PessoaJuridica(
        razao_social="",
        nome_fantasia="",
        cnpj="",
        email="",
        telefone=""
    )

    limpar()
    print(f"{'-'*20} Informe os dados do usuário {'-'*20}")
    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf = input("Informe o CPF").strip()
    usuario.email = input("Informe o e-mail: ").strip().lower()
    usuario.telefone = input("Informe o telefone: ").strip()

    limpar()
    print(f"{''*20} Informe os dados da empresa {'-'*20}")
    empresa.razao_social = input("Informe a razão social: ").strip()
    empresa.nome_fantasia = input("Informe o nome: ").strip().title()
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.email = input("Informe o e-mail: ").strip().lower()
    empresa.telefone = input("Informe o telefone: ").strip()

    limpar()
    print(f"{'-'*20} DADOS DO USUÁRIO {'-'*20}")
    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
    print(f"E-mail: {usuario.email}")
    print(f"Telefone: {usuario.telefone}")
    print(f"{'-'*20} DADOS DA EMPRESA {'-'*20}")
    print(f"Razão Social: {empresa.razao_social}")
    print(f"Nome da empresa: {empresa.nome_fantasia}")
    print(f"CNPJ: {empresa.cnpj}")
    print(f"E-mail: {empresa.email}")
    print(f"Telefone: {empresa.telefone}")


if __name__ == "__main__":
    main()