from dataclasses import dataclass


@dataclass
class Pessoa:
    # atributos
    nome: str
    cpf: str
    email: str
    idade: int
    altura: float