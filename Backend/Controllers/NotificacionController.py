from fastapi import APIRouter
from Services.NotificacionService import NotificacionService
from Views.NotificacionView import NotificacionView

router = APIRouter()

notificacion_service = NotificacionService()


@router.get("/notificaciones/mail")
def obtener_mail(token: str):
    datos = notificacion_service.obtener_mail(token)

    return NotificacionView.mostrar_mail(datos)


@router.get("/notificaciones/mensaje")
def obtener_mensaje(token: str):
    datos = notificacion_service.obtener_mensaje(token)

    return NotificacionView.mostrar_mensaje(datos)


@router.get("/notificaciones/whatsapp")
def obtener_whatsapp(token: str):
    datos = notificacion_service.obtener_whatsapp(token)

    return NotificacionView.mostrar_whatsapp(datos)


@router.post("/notificaciones/mail")
def enviar_mail(token: str, mensaje: str):
    datos = notificacion_service.enviar_mail(
        token,
        mensaje
    )

    return NotificacionView.mostrar_notificacion(datos)


@router.post("/notificaciones/mensaje")
def enviar_mensaje(token: str, mensaje: str):
    datos = notificacion_service.enviar_mensaje(
        token,
        mensaje
    )

    return NotificacionView.mostrar_notificacion(datos)


@router.post("/notificaciones/whatsapp")
def enviar_whatsapp(token: str, mensaje: str):
    datos = notificacion_service.enviar_whatsapp(
        token,
        mensaje
    )

    return NotificacionView.mostrar_notificacion(datos)