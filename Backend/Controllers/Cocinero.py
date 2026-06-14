from Backend.Controllers.Empleado import Empleado
from Backend.Controllers.EstadoPedido import EstadoPedido
from Pedido import Pedido
class Cocinero(Empleado):
    def __init__(self, nombre, apellido, id_empleado):
        super().__init__(nombre, apellido, id_empleado)
        
    def prepararPedido(self, pedido : Pedido):
        pedido.estado = EstadoPedido.PREPARANDO
        print(f"Cocinero {self.nombre} está preparando el pedido {pedido.id_pedido}")
        
    def marcarPedidoListo(self, pedido : Pedido):
        pedido.estado = EstadoPedido.LISTOENTREGAR
        print(f"Cocinero {self.nombre} ha marcado el pedido {pedido.id_pedido} como listo")