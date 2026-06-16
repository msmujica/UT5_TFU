from Database.connection import get_connection


class EstadisticaRepository:

    def obtener_resumen_ventas_hoy(self):
        conexion = get_connection()
        cursor = conexion.cursor()

        query = """
            SELECT
                COALESCE(SUM(total), 0) AS total_vendido,
                COUNT(*) AS cantidad_pedidos,
                COALESCE(AVG(total), 0) AS ticket_promedio
            FROM pedido
            WHERE DATE(fecha_hora) = CURDATE()
            AND estado <> 'CANCELADO'
        """

        cursor.execute(query)
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        return resultado


    def obtener_pedidos_por_estado_hoy(self):
        conexion = get_connection()
        cursor = conexion.cursor()

        query = """
            SELECT
                estado,
                COUNT(*) AS cantidad
            FROM pedido
            WHERE DATE(fecha_hora) = CURDATE()
            GROUP BY estado
        """

        cursor.execute(query)
        resultados = cursor.fetchall()

        cursor.close()
        conexion.close()

        return resultados


    def obtener_producto_mas_vendido_hoy(self):
        conexion = get_connection()
        cursor = conexion.cursor()

        query = """
            SELECT
                p.id_producto,
                p.nombre,
                SUM(dp.cantidad) AS cantidad_vendida
            FROM detalle_pedido dp
            INNER JOIN producto p
                ON dp.id_producto = p.id_producto
            INNER JOIN pedido pe
                ON dp.id_pedido = pe.id_pedido
            WHERE DATE(pe.fecha_hora) = CURDATE()
            AND pe.estado <> 'CANCELADO'
            GROUP BY p.id_producto, p.nombre
            ORDER BY cantidad_vendida DESC
            LIMIT 1
        """

        cursor.execute(query)
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        return resultado
    
    def obtener_resumen_ventas_mes(self):
        conexion = get_connection()
        cursor = conexion.cursor()

        query = """
            SELECT
                COALESCE(SUM(total), 0) AS total_vendido,
                COUNT(*) AS cantidad_pedidos,
                COALESCE(AVG(total), 0) AS ticket_promedio
            FROM pedido
            WHERE YEAR(fecha_hora) = YEAR(CURDATE())
            AND MONTH(fecha_hora) = MONTH(CURDATE())
            AND estado <> 'CANCELADO'
        """

        cursor.execute(query)
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        return resultado


    def obtener_pedidos_por_estado_mes(self):
        conexion = get_connection()
        cursor = conexion.cursor()

        query = """
            SELECT
                estado,
                COUNT(*) AS cantidad
            FROM pedido
            WHERE YEAR(fecha_hora) = YEAR(CURDATE())
            AND MONTH(fecha_hora) = MONTH(CURDATE())
            GROUP BY estado
        """

        cursor.execute(query)
        resultados = cursor.fetchall()

        cursor.close()
        conexion.close()

        return resultados