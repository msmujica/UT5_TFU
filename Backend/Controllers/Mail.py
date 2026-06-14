from Backend.Controllers.INotificacion import INotificacion

class Mail(INotificacion):
    def __init__(self, token):
        self.token = token
        

    def enviar_notificacion(self, mensaje):
        print(f"Enviando notificación por mail: {mensaje}")