from Backend.Controllers.EstadoPedido import EstadoPedido
from Backend.Controllers.Producto import Producto
from Backend.Controllers.ItemProducto import ItemProducto
class Pedido():
    def __init__(self, id_pedido, fecha, productos: list[ItemProducto]):
        self.id_pedido = id_pedido
        self.fecha = fecha
        self.estado = EstadoPedido.PAGANDO
        self.productos = productos
    
    def agregar_producto(self, item: Producto, cantidad):
        producto = ItemProducto(item, cantidad)
        self.productos.append(producto)
        
    def eliminar_producto(self, item: ItemProducto):
        self.productos.remove(item)
    
    