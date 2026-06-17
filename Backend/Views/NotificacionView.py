class NotificacionView:
    
    @staticmethod
    def mostrar_mail(mail):
        return {
            "tipo": "Mail",
            "token": mail.token
        }

    @staticmethod
    def mostrar_mensaje(mensaje):
        return {
            "tipo": "Mensaje",
            "token": mensaje.token
        }

    @staticmethod
    def mostrar_whatsapp(whatsapp):
        return {
            "tipo": "Whatsapp",
            "token": whatsapp.token
        }