# classe
class Pessoa:
    # construtor
    def __init__(self,nome,idade,email,cpf):
        # atributos
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cpf = cpf

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"E-mail: {self.email}")
        print(f"CPF: {self.cpf}")


def main():
    # instanciar a classe
    usuario = Pessoa(nome="",idade=0,email="",cpf="")

    # insere valores nos atributos
    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.idade = int(input("Informe a idade: "))
    usuario.email = input("Informe o e-mail: ").strip().lower()
    usuario.cpf = input("Informe o CPF: ").strip()

    # exibe os atributos na tela
    usuario.exibir_dados()

if __name__ == "__main__":
    main()