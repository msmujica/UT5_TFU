from Models.Mail import Mail
from Models.Mensaje import Mensaje
from Models.Whatsapp import Whatsapp


class NotificacionService:

    def enviar_mail(self, token, mensaje):
        mail = Mail(token)
        mail.enviar_notificacion(mensaje)

        return {
            "canal": "Mail",
            "mensaje": mensaje
        }

    def enviar_mensaje(self, token, mensaje):
        mensaje_obj = Mensaje(token)
        mensaje_obj.enviar_notificacion(mensaje)

        return {
            "canal": "Mensaje",
            "mensaje": mensaje
        }

    def enviar_whatsapp(self, token, mensaje):
        whatsapp = Whatsapp(token)
        whatsapp.enviar_notificacion(mensaje)

        return {
            "canal": "Whatsapp",
            "mensaje": mensaje
        }