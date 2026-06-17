from Models.IMetodoPago import MetodoPago

class Tarjeta(MetodoPago):
    def __init__(self, numero_tarjeta, fecha_expiracion, codigo_seguridad):
        self.numero_tarjeta = numero_tarjeta
        self.fecha_expiracion = fecha_expiracion
        self.codigo_seguridad = codigo_seguridad
        
    def procesar_pago(self, monto):
        print(f"Procesando pago de {monto} con tarjeta {self.numero_tarjeta}")