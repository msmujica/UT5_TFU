MEDIOS_VALIDOS = {"EFECTIVO", "TARJETA", "TRANSFERENCIA", "MERCADO_PAGO"}


class PagoFactory:
    @staticmethod
    def crear(medio_pago: str):
        if medio_pago not in MEDIOS_VALIDOS:
            raise ValueError(f"Medio de pago no soportado: {medio_pago}")
        return medio_pago
