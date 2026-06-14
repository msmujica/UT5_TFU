from EstadoPedido import EstadoPedido
from Pedido import Pedido
class GestorPedido():
    def __init__(self):
        self.pedido = Pedido
        
        
    def confirmarPedido(self):
        print(self.pedido.estado)
    
    def cambiarEstado(self, nuevo_estado : EstadoPedido):
        self.pedido.estado = nuevo_estado