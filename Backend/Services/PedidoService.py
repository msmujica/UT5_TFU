from Repositories.PedidoRepositories import PedidoRepository


class PedidoService:

    def __init__(self):
        self.pedido_repository = PedidoRepository()

    def obtener_pedidos_en_preparacion(self):
        pedidos = self.pedido_repository.obtener_pedidos_en_preparacion()
        return pedidos

    def obtener_pedidos_del_dia_por_estado(self):
        pedidos = self.pedido_repository.obtener_pedidos_del_dia()

        pedidos_por_estado = {
            "PENDIENTE": [],
            "EN_PREPARACION": [],
            "LISTO": [],
            "ENTREGADO": [],
            "CANCELADO": []
        }

        for pedido in pedidos:
            estado = pedido.estado

            if estado in pedidos_por_estado:
                pedidos_por_estado[estado].append(pedido)
            else:
                pedidos_por_estado[estado] = [pedido]

        return pedidos_por_estado