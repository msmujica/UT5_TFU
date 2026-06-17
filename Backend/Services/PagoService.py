from Database.connection import get_connection


class PagoService:

    # =========================
    # CREATE
    # =========================
    def crear_pago(self, id_pedido, medio_pago, monto, estado_pago="APROBADO"):

        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO pago (id_pedido, medio_pago, estado_pago, monto)
                    VALUES (%s, %s, %s, %s)
                """, (id_pedido, medio_pago, estado_pago, monto))

                pago_id = cursor.lastrowid

            connection.commit()

            return self.obtener_pago_por_id(pago_id)

        finally:
            connection.close()

    # =========================
    # GET ALL
    # =========================
    def obtener_pagos(self):

        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM pago
                    ORDER BY fecha_hora DESC
                """)
                return cursor.fetchall()

        finally:
            connection.close()

    # =========================
    # GET BY ID
    # =========================
    def obtener_pago_por_id(self, id_pago):

        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM pago
                    WHERE id_pago = %s
                    LIMIT 1
                """, (id_pago,))

                return cursor.fetchone()

        finally:
            connection.close()

    # =========================
    # GET BY PEDIDO
    # =========================
    def obtener_pagos_por_pedido(self, id_pedido):

        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM pago
                    WHERE id_pedido = %s
                    ORDER BY fecha_hora DESC
                """, (id_pedido,))

                return cursor.fetchall()

        finally:
            connection.close()