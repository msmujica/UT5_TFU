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
    
    def crear_producto(self, nombre, descripcion, precio, disponible):
        conexion = get_connection()
        cursor = conexion.cursor()

        query = """
            INSERT INTO producto (
                nombre,
                descripcion,
                precio,
                activo
            )
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(query, (
            nombre,
            descripcion,
            precio,
            disponible
        ))

        conexion.commit()

        id_producto = cursor.lastrowid

        cursor.close()
        conexion.close()

        return Producto(
            id_producto=id_producto,
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            disponible=disponible
        )

    def modificar_producto(self, id_producto, nombre, descripcion, precio, disponible):
        conexion = get_connection()
        cursor = conexion.cursor()

        query = """
            UPDATE producto
            SET nombre = %s,
                descripcion = %s,
                precio = %s,
                activo = %s
            WHERE id_producto = %s
        """

        cursor.execute(query, (
            nombre,
            descripcion,
            precio,
            disponible,
            id_producto
        ))

        conexion.commit()

        cursor.close()
        conexion.close()

        return Producto(
            id_producto=id_producto,
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            disponible=disponible
        )

    def eliminar_producto(self, id_producto):
        conexion = get_connection()
        cursor = conexion.cursor()

        query = """
            DELETE FROM producto
            WHERE id_producto = %s
        """

        cursor.execute(query, (id_producto,))
        conexion.commit()

        cursor.close()
        conexion.close()

        return True