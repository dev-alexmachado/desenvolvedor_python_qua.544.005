class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def cumprimentar(self):
        return f"Olá, boa tarde. Meu nome é {self.nome}, tenho {self.idade} anos, e meu e-mail é {self.email}."