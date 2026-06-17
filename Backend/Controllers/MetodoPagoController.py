from fastapi import APIRouter
from Services.MetodoPagoService import MetodoPagoService

router = APIRouter()
service = MetodoPagoService()

# ==================================================
# POST - PROCESAR PAGOS
# ==================================================

@router.post("/pagos/efectivo")
def pagar_efectivo(id_pedido: int, monto: float, monto_entregado: float):
    return service.procesar_pago_efectivo(id_pedido, monto, monto_entregado)


@router.post("/pagos/tarjeta")
def pagar_tarjeta(
    id_pedido: int,
    monto: float,
    numero_tarjeta: str,
    fecha_expiracion: str,
    codigo_seguridad: str
):
    return service.procesar_pago_tarjeta(
        id_pedido,
        monto,
        numero_tarjeta,
        fecha_expiracion,
        codigo_seguridad
    )


@router.post("/pagos/mercadopago")
def pagar_mercadopago(id_pedido: int, monto: float, token: str):
    return service.procesar_pago_mercadopago(id_pedido, monto, token)

# ==================================================
# GET - CONSULTAR PAGOS EN BASE DE DATOS
# ==================================================

@router.get("/pagos/{id_pago}")
def obtener_pago(id_pago: int):
    return service.obtener_pago_por_id(id_pago)


@router.get("/pagos/pedido/{id_pedido}")
def obtener_pagos_por_pedido(id_pedido: int):
    return service.obtener_pagos_por_pedido(id_pedido)