from Models.IMetodoPago import MetodoPago

class MercadoPago(MetodoPago):
    def __init__(self, token):
        self.token = token

    def procesar_pago(self, monto):
        print(f"Procesando pago con MercadoPago de {monto}")