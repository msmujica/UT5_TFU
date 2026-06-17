class PedidoView:

    @staticmethod
    def mostrar_pedido(pedido):
        return {
            "id_pedido": pedido.id_pedido,
            "cliente": pedido.cliente,
            "estado": pedido.estado,
            "total": pedido.total,
            "fecha": str(pedido.fecha)
        }

    @staticmethod
    def mostrar_pedido_registrado(pedido, items):
        return {
            "mensaje": "Pedido registrado exitosamente",
            "id_pedido": pedido.id_pedido,
            "cliente": pedido.cliente,
            "estado": pedido.estado,
            "total": pedido.total,
            "items": items
        }

    @staticmethod
    def mostrar_pedido_cancelado(pedido, razon):
        return {
            "mensaje": "Pedido cancelado",
            "id_pedido": pedido.id_pedido,
            "estado": pedido.estado,
            "razon": razon
        }

    @staticmethod
    def mostrar_pedidos_en_preparacion(pedidos):
        return {
            "cantidad": len(pedidos),
            "pedidos": [
                PedidoView.mostrar_pedido(pedido)
                for pedido in pedidos
            ]
        }

    @staticmethod
    def mostrar_pedidos_por_estado(pedidos_por_estado):
        return {
            "resumen": {
                "pendientes": len(pedidos_por_estado.get("PENDIENTE", [])),
                "en_preparacion": len(pedidos_por_estado.get("EN_PREPARACION", [])),
                "listos": len(pedidos_por_estado.get("LISTO", [])),
                "entregados": len(pedidos_por_estado.get("ENTREGADO", [])),
                "cancelados": len(pedidos_por_estado.get("CANCELADO", []))
            },
            "pedidos": {
                "pendientes": [
                    PedidoView.mostrar_pedido(pedido)
                    for pedido in pedidos_por_estado.get("PENDIENTE", [])
                ],
                "en_preparacion": [
                    PedidoView.mostrar_pedido(pedido)
                    for pedido in pedidos_por_estado.get("EN_PREPARACION", [])
                ],
                "listos": [
                    PedidoView.mostrar_pedido(pedido)
                    for pedido in pedidos_por_estado.get("LISTO", [])
                ],
                "entregados": [
                    PedidoView.mostrar_pedido(pedido)
                    for pedido in pedidos_por_estado.get("ENTREGADO", [])
                ],
                "cancelados": [
                    PedidoView.mostrar_pedido(pedido)
                    for pedido in pedidos_por_estado.get("CANCELADO", [])
                ]
            }
        }
