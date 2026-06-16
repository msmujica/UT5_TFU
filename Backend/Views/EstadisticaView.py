from datetime import date


class EstadisticaView:

    @staticmethod
    def mostrar_rendimiento_hoy(datos):
        producto = datos["producto_mas_vendido"]

        return {
            "fecha": str(date.today()),
            "total_vendido": float(datos["total_vendido"]),
            "cantidad_pedidos": int(datos["cantidad_pedidos"]),
            "ticket_promedio": float(datos["ticket_promedio"]),
            "pedidos_por_estado": datos["pedidos_por_estado"],
            "producto_mas_vendido": None if producto is None else {
                "id_producto": producto["id_producto"],
                "nombre": producto["nombre"],
                "cantidad_vendida": int(producto["cantidad_vendida"])
            }
        }
    
    @staticmethod
    def mostrar_rendimiento_mes(datos):
        hoy = date.today()

        return {
            "mes": hoy.month,
            "anio": hoy.year,
            "total_vendido": float(datos["total_vendido"]),
            "cantidad_pedidos": int(datos["cantidad_pedidos"]),
            "ticket_promedio": float(datos["ticket_promedio"]),
            "pedidos_por_estado": datos["pedidos_por_estado"]
        }