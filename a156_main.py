# Enum -> Enumerações
import enum


class Direcoes(enum.Enum):
    ACIMA = enum.auto()
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ABAIXO = enum.auto()


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError("Direção não encontrada")

    print(f"Movendo para {direcao.name} ({direcao.value})")


mover(Direcoes.ACIMA)
mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ABAIXO)
