from Backend.Controllers.INotificacion import INotificacion

class Mensaje(INotificacion):
    def __init__(self, token):
        self.token = token
        

    def enviar_notificacion(self, mensaje):
        print(f"Enviando notificación por mensaje: {mensaje}")