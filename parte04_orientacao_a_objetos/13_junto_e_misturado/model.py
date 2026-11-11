from abc import ABC,abstractmethod
from dataclasses import dataclass


# interface
class IConta(ABC):
    @abstractmethod
    def consultar(self):
        pass

    @abstractmethod
    def depositar(self,valor):
        pass

    @abstractmethod
    def sacar(self,valor):
        pass


@dataclass
class Pessoa:
    nome: str
    cpf: str

    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}"

    def __del__(self):
        print(f"Objeto {self.nome} destruído com sucesso!")


@dataclass
class Conta(IConta):
    agencia: str
    n_conta: str
    tipo_conta: str
    saldo: float
    titular: Pessoa

    def __str__(self):
        return f"Conta {self.n_conta} criada com sucesso!"

    def __float__(self):
        return self.saldo

    def __del__(self):
        print("Conta destruída com sucesso!")

    def consultar(self):
        print("Titular da conta:")
        print(self.titular)
        print(f"Agência: {self.agencia}")
        print(f"Número da conta: {self.n_conta}")
        print(f"Saldo: R$ {self.saldo:.2f}")
        print(f"Tipo de conta: {self.tipo_conta}")

    def depositar(self,valor):
        self.saldo += valor
        return self.saldo

    def sacar(self,valor):
        self.saldo -= valor
        return self.saldo


@dataclass
class ContaCorrente(Conta):
    taxa: float

    def sacar(self,valor):
        self.saldo -= self.taxa
        return super().sacar(valor)


@dataclass
class ContaPoupanca(Conta):
    juros: float

    def depositar(self,valor):
        self.saldo += self.saldo*(self.juros/100)
        return super().depositar(valor)