class Pago:
    
    def __init__(self, id_pago, id_pedido, medio_pago, estado_pago, monto, fecha_hora):
        self.id_pago = id_pago
        self.id_pedido = id_pedido
        self.medio_pago = medio_pago
        self.estado_pago = estado_pago
        self.monto = monto
        self.fecha_hora = fecha_hora