from Repositories.EstadisticaRepositories import EstadisticaRepository


class EstadisticaService:

    def __init__(self):
        self.estadistica_repository = EstadisticaRepository()

    def obtener_rendimiento_hoy(self):
        resumen = self.estadistica_repository.obtener_resumen_ventas_hoy()
        estados = self.estadistica_repository.obtener_pedidos_por_estado_hoy()
        producto_mas_vendido = self.estadistica_repository.obtener_producto_mas_vendido_hoy()

        pedidos_por_estado = {
            "PENDIENTE": 0,
            "EN_PREPARACION": 0,
            "LISTO": 0,
            "ENTREGADO": 0,
            "CANCELADO": 0
        }

        for fila in estados:
            pedidos_por_estado[fila["estado"]] = fila["cantidad"]

        return {
            "total_vendido": resumen["total_vendido"],
            "cantidad_pedidos": resumen["cantidad_pedidos"],
            "ticket_promedio": resumen["ticket_promedio"],
            "pedidos_por_estado": pedidos_por_estado,
            "producto_mas_vendido": producto_mas_vendido
        }
    def obtener_rendimiento_mes(self):
        resumen = self.estadistica_repository.obtener_resumen_ventas_mes()
        estados = self.estadistica_repository.obtener_pedidos_por_estado_mes()

        pedidos_por_estado = {
            "PENDIENTE": 0,
            "EN_PREPARACION": 0,
            "LISTO": 0,
            "ENTREGADO": 0,
            "CANCELADO": 0
        }

        for fila in estados:
            pedidos_por_estado[fila["estado"]] = fila["cantidad"]

        return {
            "total_vendido": resumen["total_vendido"],
            "cantidad_pedidos": resumen["cantidad_pedidos"],
            "ticket_promedio": resumen["ticket_promedio"],
            "pedidos_por_estado": pedidos_por_estado
        }