# classes
class Endereco:
    def __init__(self,cep,uf,cidade,bairro,logradouro,complemento,numero):
        self.__cep = cep
        self.__uf = uf
        self.__cidade = cidade
        self.__bairro = bairro
        self.__logradouro = logradouro
        self.__complemento = complemento
        self.__numero = numero

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self,cep):
        self.__cep = cep

    @property
    def uf(self):
        return self.__uf

    @uf.setter
    def uf(self,uf):
        self.__uf = uf

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self,cidade):
        self.__cidade = cidade

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self,bairro):
        self.__bairro = bairro

    @property
    def logradouro(self):
        return self.__logradouro

    @logradouro.setter
    def logradouro(self,logradouro):
        self.__logradouro = logradouro

    @property
    def complemento(self):
        return self.__complemento

    @complemento.setter
    def complemento(self,complemento):
        self.__complemento = complemento

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self,numero):
        self.__numero = numero

    # método
    def obter_endereco(self):
        return f"CEP: {self.__cep}\nUF: {self.__uf}\nCidade: {self.__cidade}\nBairro: {self.__bairro}\nLogradouro: {self.__logradouro}\nComplemento: {self.__complemento}\nNúmero: {self.__numero}"


class Pessoa:
    def __init__(self,nome,cpf,email,telefone,endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone
        self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,email):
        self.__email = email

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self,telefone):
        self.__telefone = telefone

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self,endereco):
        self.__endereco = endereco

    # método
    def exibir_dados(self):
        print(f"Nome: {self.__nome}")
        print(f"CPF: {self.__cpf}")
        print(f"E-mail: {self.__email}")
        print(f"Telefone: {self.__telefone}")
        print(f"Endereço: {self.__endereco.obter_endereco()}")