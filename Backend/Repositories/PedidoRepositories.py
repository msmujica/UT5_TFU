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

    def obtener_productos_por_ids(self, ids: list):
        if not ids:
            return []

        conexion = get_connection()
        cursor = conexion.cursor()

        placeholders = ", ".join(["%s"] * len(ids))
        cursor.execute(
            f"SELECT id_producto, nombre, precio, activo FROM producto WHERE id_producto IN ({placeholders})",
            ids
        )
        resultados = cursor.fetchall()

        cursor.close()
        conexion.close()

        return resultados

    def registrar_pedido(self, celular_cliente, id_empleado, medio_pago, items_calculados):
        conexion = get_connection()
        cursor = conexion.cursor()

        try:
            total = sum(item["subtotal"] for item in items_calculados)

            cursor.execute(
                "INSERT INTO pedido (celular_cliente, estado, total, id_empleado) VALUES (%s, 'PENDIENTE', %s, %s)",
                (celular_cliente, total, id_empleado)
            )
            id_pedido = cursor.lastrowid

            for item in items_calculados:
                cursor.execute(
                    "INSERT INTO detalle_pedido (id_pedido, id_producto, cantidad, precio_unitario, subtotal) VALUES (%s, %s, %s, %s, %s)",
                    (id_pedido, item["id_producto"], item["cantidad"], item["precio_unitario"], item["subtotal"])
                )

            cursor.execute(
                "INSERT INTO pago (id_pedido, medio_pago, estado_pago, monto) VALUES (%s, %s, 'PENDIENTE', %s)",
                (id_pedido, medio_pago, total)
            )

            conexion.commit()

            return Pedido(
                id_pedido=id_pedido,
                cliente=celular_cliente,
                estado="PENDIENTE",
                total=total,
                fecha=None
            )

        except Exception as e:
            conexion.rollback()
            raise e

        finally:
            cursor.close()
            conexion.close()

    def cancelar_pedido(self, id_pedido):
        conexion = get_connection()
        cursor = conexion.cursor()

        try:
            cursor.execute(
                "SELECT id_pedido, celular_cliente, estado, total, fecha_hora FROM pedido WHERE id_pedido = %s",
                (id_pedido,)
            )
            fila = cursor.fetchone()

            if not fila:
                raise ValueError(f"Pedido {id_pedido} no encontrado")

            if fila["estado"] not in ("PENDIENTE",):
                raise ValueError(f"No se puede cancelar un pedido en estado {fila['estado']}")

            cursor.execute(
                "UPDATE pedido SET estado = 'CANCELADO' WHERE id_pedido = %s",
                (id_pedido,)
            )
            conexion.commit()

            return Pedido(
                id_pedido=fila["id_pedido"],
                cliente=fila["celular_cliente"],
                estado="CANCELADO",
                total=fila["total"],
                fecha=fila["fecha_hora"]
            )

        except Exception as e:
            conexion.rollback()
            raise e

        finally:
            cursor.close()
            conexion.close()