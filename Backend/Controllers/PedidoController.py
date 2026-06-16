from fastapi import APIRouter, HTTPException
from Services.PedidoService import PedidoService
from Views.PedidoView import PedidoView
from Models.PedidoModel import RegistrarPedidoSchema

router = APIRouter()

pedido_service = PedidoService()


@router.post("/pedidos", status_code=201)
def registrar_pedido(datos: RegistrarPedidoSchema):
    try:
        pedido, items = pedido_service.registrar_pedido(datos)
        return PedidoView.mostrar_pedido_registrado(pedido, items)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/pedidos/en-preparacion")
def obtener_pedidos_en_preparacion():
    pedidos = pedido_service.obtener_pedidos_en_preparacion()

    return PedidoView.mostrar_pedidos_en_preparacion(pedidos)


@router.get("/pedidos/hoy")
def obtener_pedidos_del_dia():
    pedidos_por_estado = pedido_service.obtener_pedidos_del_dia_por_estado()

    return PedidoView.mostrar_pedidos_por_estado(pedidos_por_estado)