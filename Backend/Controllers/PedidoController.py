from fastapi import APIRouter
from Services.PedidoService import PedidoService
from Views.PedidoView import PedidoView

router = APIRouter()

pedido_service = PedidoService()


@router.get("/pedidos/en-preparacion")
def obtener_pedidos_en_preparacion():
    pedidos = pedido_service.obtener_pedidos_en_preparacion()

    return PedidoView.mostrar_pedidos_en_preparacion(pedidos)

@router.get("/pedidos/hoy")
def obtener_pedidos_del_dia():
    pedidos_por_estado = pedido_service.obtener_pedidos_del_dia_por_estado()

    return PedidoView.mostrar_pedidos_por_estado(pedidos_por_estado)