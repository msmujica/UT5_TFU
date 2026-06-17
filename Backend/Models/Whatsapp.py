from Models.INotificacion import INotificacion

class Whatsapp(INotificacion):
    def __init__(self, token):
        self.token = token
        

    def enviar_notificacion(self, mensaje):
        print(f"Enviando notificación por Whatsapp: {mensaje}")