from fastapi import APIRouter
from Services.ProductoService import ProductoService
from Views.ProductoView import ProductoView

router = APIRouter()

producto_service = ProductoService()


@router.get("/productos/menu")
def obtener_menu():
    productos = producto_service.obtener_menu()

    return ProductoView.mostrar_menu(productos)