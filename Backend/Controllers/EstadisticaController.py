from fastapi import APIRouter
from Services.EstadisticaService import EstadisticaService
from Views.EstadisticaView import EstadisticaView

router = APIRouter()

estadistica_service = EstadisticaService()


@router.get("/estadisticas/rendimiento-dia")
def obtener_rendimiento_hoy():
    datos = estadistica_service.obtener_rendimiento_hoy()

    return EstadisticaView.mostrar_rendimiento_hoy(datos)

@router.get("/estadisticas/rendimiento-mes")
def obtener_rendimiento_mes():
    datos = estadistica_service.obtener_rendimiento_mes()

    return EstadisticaView.mostrar_rendimiento_mes(datos)