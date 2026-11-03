# classe
class Pessoa:
    def __init__(self,nome,idade,cpf,telefone,email):
        self.__nome = nome 
        self.__idade = idade
        self.__cpf = cpf
        self.__telefone = telefone
        self.__email = email

    # métodos set e get
    @property # método get
    def nome(self):
        return self.__nome

    @nome.setter # método set
    def nome(self,nome):
        self.__nome = nome

    @property # método get
    def idade(self):
        return self.__idade

    @idade.setter # método set
    def idade(self,idade):
        self.__idade = idade

    @property # método get
    def cpf(self):
        return self.__cpf

    @cpf.setter # método set
    def cpf(self,cpf):
        self.__cpf = cpf

    @property # método get
    def telefone(self):
        return self.__telefone

    @telefone.setter # método set
    def telefone(self,telefone):
        self.__telefone = telefone

    @property # método get
    def email(self):
        return self.__email

    @email.setter # método set
    def email(self,email):
        self.__email = email