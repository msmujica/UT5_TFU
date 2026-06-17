
from abc import abstractmethod


class INotificacion():
    
    @abstractmethod
    def enviar_notificacion(self, mensaje):
        pass