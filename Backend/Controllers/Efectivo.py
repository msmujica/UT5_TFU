from Backend.Controllers.IMetodoPago import MetodoPago

class Efectivo(MetodoPago):
    def __init__(self, monto_entregado):
        self.monto_entregado = monto_entregado

    def procesar_pago(self, monto):
        print(f"Procesando pago en efectivo de {monto}")