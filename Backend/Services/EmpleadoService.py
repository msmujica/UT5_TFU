from Repositories.PedidoRepositories import PedidoRepository


class EmpleadoService:

    def __init__(self):
        self.pedido_repository = PedidoRepository()

    def marcar_pedido_listo(self, id_pedido: int):
        pedido = self.pedido_repository.obtener_pedido_por_id(id_pedido)

        if pedido is None:
            raise ValueError("El pedido no existe")

        if pedido.estado != "EN_PREPARACION":
            raise ValueError("Solo se puede marcar como listo un pedido en preparación")

        return self.pedido_repository.actualizar_estado_pedido(id_pedido, "LISTO")

    def entregar_pedido(self, id_pedido: int):
        pedido = self.pedido_repository.obtener_pedido_por_id(id_pedido)

        if pedido is None:
            raise ValueError("El pedido no existe")

        if pedido.estado != "LISTO":
            raise ValueError("Solo se puede entregar un pedido que esté listo")

        return self.pedido_repository.actualizar_estado_pedido(id_pedido, "ENTREGADO")

    def recibir_pedido(self, id_pedido: int):
        pedido = self.pedido_repository.obtener_pedido_por_id(id_pedido)

        if pedido is None:
            raise ValueError("El pedido no existe")

        if pedido.estado != "PENDIENTE":
            raise ValueError("Solo se puede recibir un pedido pendiente")

        return self.pedido_repository.actualizar_estado_pedido(id_pedido, "EN_PREPARACION")