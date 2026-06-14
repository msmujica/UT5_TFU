from Empleado import Empleado
from Pedido import Pedido
from EstadoPedido import EstadoPedido
class Cajero(Empleado):
    def __init__(self, nombre, apellido, id_empleado):
        super().__init__(nombre, apellido, id_empleado)
        
    def entregarPedido(self, pedido:Pedido):
        pedido.estado = EstadoPedido.ENTREGADO
        print(f"Cajero {self.nombre} está entregando el pedido {pedido.id_pedido}")
        
    def recibirPedido(self, pedido:Pedido):
        pedido.estado = EstadoPedido.PENDIENTE
        print(f"Cajero {self.nombre} ha registrado el pedido {pedido.id_pedido}")
    