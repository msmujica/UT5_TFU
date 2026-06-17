from Models.Efectivo import Efectivo
from Models.Tarjeta import Tarjeta
from Models.MercadoPago import MercadoPago
from Database.connection import get_connection


class MetodoPagoService:

    # ==================================================
    # INSERTAR PAGO (BASE DE DATOS REAL)
    # ==================================================

    def _insertar_pago(self, id_pedido, medio_pago, monto):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO pago (id_pedido, medio_pago, estado_pago, monto)
                    VALUES (%s, %s, 'APROBADO', %s)
                """, (id_pedido, medio_pago, monto))

                pago_id = cursor.lastrowid

            connection.commit()

            return pago_id

        finally:
            connection.close()

    # ==================================================
    # PROCESAR PAGOS (POST)
    # ==================================================

    def procesar_pago_efectivo(self, id_pedido, monto, monto_entregado):
        efectivo = Efectivo(monto_entregado)
        efectivo.procesar_pago(monto)

        pago_id = self._insertar_pago(id_pedido, "EFECTIVO", monto)

        return self._get_pago_by_id(pago_id)

    def procesar_pago_tarjeta(self, id_pedido, monto, numero_tarjeta, fecha_expiracion, codigo_seguridad):
        tarjeta = Tarjeta(numero_tarjeta, fecha_expiracion, codigo_seguridad)
        tarjeta.procesar_pago(monto)

        pago_id = self._insertar_pago(id_pedido, "TARJETA", monto)

        return self._get_pago_by_id(pago_id)

    def procesar_pago_mercadopago(self, id_pedido, monto, token):
        mp = MercadoPago(token)
        mp.procesar_pago(monto)

        pago_id = self._insertar_pago(id_pedido, "MERCADO_PAGO", monto)

        return self._get_pago_by_id(pago_id)

    # ==================================================
    # GET DESDE BASE DE DATOS
    # ==================================================

    def obtener_pago_por_id(self, id_pago):
        return self._get_pago_by_id(id_pago)

    def obtener_pagos_por_pedido(self, id_pedido):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM pago
                    WHERE id_pedido = %s
                """, (id_pedido,))

                return cursor.fetchall()

        finally:
            connection.close()

    # ==================================================
    # PRIVATE GET
    # ==================================================

    def _get_pago_by_id(self, id_pago):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM pago
                    WHERE id_pago = %s
                """, (id_pago,))

                return cursor.fetchone()

        finally:
            connection.close()