# from dataclasses import dataclass


"""@dataclass
class Pessoa:
    nome: str
    idade: int


if __name__ == "__main__":
    p1 = Pessoa("Luiz", 30)
    p2 = Pessoa("Luiz", 30)
    print(p1 == p2)"""


# dataclasses com métodos, property e setter
"""@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"


if __name__ == "__main__":
    p1 = Pessoa("Luiz", "Almeida")
    print(p1)
    print(p1.nome_completo())"""

"""#  __init__


# @dataclass
# class Pessoa:
#     nome: str
#     sobrenome: str

#     def __post_init__(self):
#         self.nome_completo = f"{self.nome} {self.sobrenome}"


# if __name__ == "__main__":
#     p1 = Pessoa("Luiz", "Almeida")
#     print(p1)"""
