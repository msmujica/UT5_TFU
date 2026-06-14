from Repositories.ProductoRepository import ProductoRepository


class ProductoService:

    def __init__(self):
        self.producto_repository = ProductoRepository()

    def obtener_menu(self):
        productos = self.producto_repository.obtener_todos_los_productos()

        return productos