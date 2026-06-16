class Pedido:

    def __init__(self, id_pedido, cliente, estado, total, fecha):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.estado = estado
        self.total = total
        self.fecha = fecha