from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class MedioPagoEnum(str, Enum):
    EFECTIVO = "EFECTIVO"
    TARJETA = "TARJETA"
    TRANSFERENCIA = "TRANSFERENCIA"
    MERCADO_PAGO = "MERCADO_PAGO"


class ItemPedidoSchema(BaseModel):
    id_producto: int
    cantidad: int


class RegistrarPedidoSchema(BaseModel):
    celular_cliente: str
    id_empleado: int
    medio_pago: MedioPagoEnum
    items: List[ItemPedidoSchema]


class CancelarPedidoSchema(BaseModel):
    razon: Optional[str] = None


class Pedido:

    def __init__(self, id_pedido, cliente, estado, total, fecha):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.estado = estado
        self.total = total
        self.fecha = fecha