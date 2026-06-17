from fastapi import APIRouter
from Services.PagoService import PagoService
from Views.PagoView import PagoView

router = APIRouter()
service = PagoService()


# =========================
# CREATE PAGO
# =========================
@router.post("/pagos")
def crear_pago(id_pedido: int, medio_pago: str, monto: float):

    pago = service.crear_pago(id_pedido, medio_pago, monto)

    return PagoView.mostrar_pago(pago)


# =========================
# GET ALL
# =========================
@router.get("/pagos")
def obtener_pagos():

    pagos = service.obtener_pagos()

    return PagoView.mostrar_lista(pagos)


# =========================
# GET BY ID
# =========================
@router.get("/pagos/{id_pago}")
def obtener_pago(id_pago: int):

    pago = service.obtener_pago_por_id(id_pago)

    return PagoView.mostrar_pago(pago)


# =========================
# GET BY PEDIDO
# =========================
@router.get("/pagos/pedido/{id_pedido}")
def pagos_por_pedido(id_pedido: int):

    pagos = service.obtener_pagos_por_pedido(id_pedido)

    return PagoView.mostrar_lista(pagos)