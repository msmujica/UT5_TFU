from Backend.Controllers.ItemProducto import ItemProducto
from Backend.Controllers.Pedido import Pedido
class CalculosPedido():
    def __init__(self, pedido: Pedido):
        self.pedido = pedido
        
        
    def calcularSubtotal(self, item: ItemProducto):
        return item.calcularSubTotal()