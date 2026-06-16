from Repositories.ProductoRepository import ProductoRepository


class ProductoService:

    def __init__(self):
        self.producto_repository = ProductoRepository()

    def obtener_menu(self):
        productos = self.producto_repository.obtener_todos_los_productos()

        return productos
    
    def crear_producto(self, nombre, descripcion, precio, disponible):
        return self.producto_repository.crear_producto(
            nombre,
            descripcion,
            precio,
            disponible
        )

    def modificar_producto(self, id_producto, nombre, descripcion, precio, disponible):
        return self.producto_repository.modificar_producto(
            id_producto,
            nombre,
            descripcion,
            precio,
            disponible
        )

    def eliminar_producto(self, id_producto):
        return self.producto_repository.eliminar_producto(id_producto)