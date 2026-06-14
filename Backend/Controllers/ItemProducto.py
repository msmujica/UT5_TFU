from Backend.Controllers.Producto import Prodcuto
class ItemProducto():
    def __init__(self, producto: Prodcuto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        
        
    def calcularSubTotal(self):
        return self.producto.precio * self.cantidad