# importa abstração
from abc import ABC, abstractmethod

# interface / classe abstrata
class IConta(ABC):
    @abstractmethod
    def consultar_conta(self):
        pass

    @abstractmethod
    def depositar(self,valor):
        pass

    @abstractmethod
    def sacar(self,valor):
        pass


# classe Conta
class Conta(IConta):
    def __init__(self,titular,cpf,agencia,n_conta,saldo):
        self.__titular = titular
        self.__cpf = cpf
        self.__agencia = agencia
        self.__n_conta = n_conta
        self.__saldo = saldo

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self,titular):
        self.__titular = titular

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf

    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self,agencia):
        self.__agencia = agencia

    @property
    def n_conta(self):
        return self.__n_conta

    @n_conta.setter
    def n_conta(self,n_conta):
        self.__n_conta = n_conta

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self,saldo):
        self.__saldo = saldo

    # métodos da interface
    def consultar_conta(self):
        print(f"{'-'*20} Dados da conta {'-'*20}")
        print(f"Nome do titular: {self.titular}")
        print(f"CPF do titular: {self.cpf}")
        print(f"Agência: {self.agencia}")
        print(f"Conta: {self.n_conta}")
        print(f"Saldo: R$ {self.saldo:.2f}")

    def depositar(self,valor):
        self.saldo += valor # incremento: saldo + valor
        return self.__saldo

    def sacar(self, valor):
        self.saldo -= valor # decremento: saldo - valor
        return self.__saldo