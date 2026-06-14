from enum import Enum, auto

class EstadoPedido(Enum):
    PAGANDO = auto()
    PENDIENTE = auto()
    PREPARANDO = auto()
    LISTOENTREGAR = auto()
    ENTREGADO = auto()