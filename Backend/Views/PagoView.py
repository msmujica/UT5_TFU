class PagoView:
    
    @staticmethod
    def mostrar_pago(pago):

        return {
            "id_pago": pago["id_pago"],
            "id_pedido": pago["id_pedido"],
            "medio_pago": pago["medio_pago"],
            "estado_pago": pago["estado_pago"],
            "monto": float(pago["monto"]),
            "fecha_hora": str(pago["fecha_hora"])
        }

    @staticmethod
    def mostrar_lista(pagos):

        return [
            {
                "id_pago": p["id_pago"],
                "id_pedido": p["id_pedido"],
                "medio_pago": p["medio_pago"],
                "estado_pago": p["estado_pago"],
                "monto": float(p["monto"]),
                "fecha_hora": str(p["fecha_hora"])
            }
            for p in pagos
        ]