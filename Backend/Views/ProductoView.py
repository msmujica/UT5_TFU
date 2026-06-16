class ProductoView:

    @staticmethod
    def mostrar_producto(producto):
        return {
            "id_producto": producto.id_producto,
            "nombre": producto.nombre,
            "descripcion": producto.descripcion,
            "precio": producto.precio,
            "disponible": bool(producto.disponible)
        }

    @staticmethod
    def mostrar_menu(productos):
        return {
            "cantidad": len(productos),
            "productos": [
                ProductoView.mostrar_producto(producto)
                for producto in productos
            ]
        }