from Database.connection import get_connection
from Models.PedidoModel import Pedido


class PedidoRepository:

    def obtener_pedidos_en_preparacion(self):
        conexion = get_connection()
        cursor = conexion.cursor()

        query = """
            SELECT 
                id_pedido,
                celular_cliente,
                estado,
                total,
                fecha_hora
            FROM pedido
            WHERE estado = %s
            ORDER BY fecha_hora ASC
        """

        cursor.execute(query, ("EN_PREPARACION",))
        resultados = cursor.fetchall()

        cursor.close()
        conexion.close()

        pedidos = []

        for fila in resultados:
            pedido = Pedido(
                id_pedido=fila["id_pedido"],
                cliente=fila["celular_cliente"],
                estado=fila["estado"],
                total=fila["total"],
                fecha=fila["fecha_hora"]
            )

            pedidos.append(pedido)

        return pedidos
    
    def obtener_pedidos_del_dia(self):
        conexion = get_connection()
        cursor = conexion.cursor()

        query = """
            SELECT 
                id_pedido,
                celular_cliente,
                estado,
                total,
                fecha_hora
            FROM pedido
            WHERE DATE(fecha_hora) = CURDATE()
            ORDER BY fecha_hora ASC
        """

        cursor.execute(query)
        resultados = cursor.fetchall()

        cursor.close()
        conexion.close()

        pedidos = []

        for fila in resultados:
            pedido = Pedido(
                id_pedido=fila["id_pedido"],
                cliente=fila["celular_cliente"],
                estado=fila["estado"],
                total=fila["total"],
                fecha=fila["fecha_hora"]
            )

            pedidos.append(pedido)

        return pedidos