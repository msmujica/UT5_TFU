from fastapi import APIRouter
from Services.ProductoService import ProductoService
from Views.ProductoView import ProductoView
from pydantic import BaseModel

router = APIRouter()

producto_service = ProductoService()

class CrearProductoRequest(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    disponible: bool


class ModificarProductoRequest(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    disponible: bool


@router.get("/productos/menu")
def obtener_menu():
    productos = producto_service.obtener_menu()

    return ProductoView.mostrar_menu(productos)

@router.post("/producto")
def crear_producto(datos: CrearProductoRequest):
    producto = producto_service.crear_producto(
        datos.nombre,
        datos.descripcion,
        datos.precio,
        datos.disponible
    )

    return ProductoView.mostrar_producto(producto)


@router.put("/producto/{id_producto}")
def modificar_producto(id_producto: int, datos: ModificarProductoRequest):
    producto = producto_service.modificar_producto(
        id_producto,
        datos.nombre,
        datos.descripcion,
        datos.precio,
        datos.disponible
    )

    return ProductoView.mostrar_producto(producto)


@router.delete("/producto/{id_producto}")
def eliminar_producto(id_producto: int):
    producto_service.eliminar_producto(id_producto)

    return {
        "mensaje": "Producto eliminado correctamente",
        "id_producto": id_producto
    }