from Database.connection import get_connection
from Models.ProductoModel import Producto


class ProductoRepository:

    def obtener_todos_los_productos(self):
        conexion = get_connection()
        cursor = conexion.cursor()

        query = """
            SELECT
                id_producto,
                nombre,
                descripcion,
                precio,
                activo
            FROM producto
            ORDER BY nombre ASC
        """

        cursor.execute(query)
        resultados = cursor.fetchall()

        cursor.close()
        conexion.close()

        productos = []

        for fila in resultados:
            producto = Producto(
                id_producto=fila["id_producto"],
                nombre=fila["nombre"],
                descripcion=fila["descripcion"],
                precio=fila["precio"],
                disponible=fila["activo"]
            )

            productos.append(producto)

        return productos