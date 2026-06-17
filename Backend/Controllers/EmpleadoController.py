
from fastapi import APIRouter, HTTPException
from Services.EmpleadoService import EmpleadoService

router = APIRouter()

empleado_service = EmpleadoService()


@router.put("/pedidos/{id_pedido}/recibir")
def recibir_pedido(id_pedido: int):
    try:
        empleado_service.recibir_pedido(id_pedido)
        return {"mensaje": "Pedido recibido y marcado en preparación"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/pedidos/{id_pedido}/listo")
def marcar_pedido_listo(id_pedido: int):
    try:
        empleado_service.marcar_pedido_listo(id_pedido)
        return {"mensaje": "Pedido marcado como listo"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/pedidos/{id_pedido}/entregar")
def entregar_pedido(id_pedido: int):
    try:
        empleado_service.entregar_pedido(id_pedido)
        return {"mensaje": "Pedido entregado correctamente"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))