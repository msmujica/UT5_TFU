from fastapi import FastAPI
from Database.connection import get_connection
from Controllers.PedidoController import router as pedido_router
from Controllers.ProductoController import router as producto_router
app = FastAPI()

app.include_router(pedido_router)
app.include_router(producto_router)

@app.get("/Health")
def home():
    return {"mensaje": "Todo bien pa"}


@app.get("/db-test")
def db_test():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT DATABASE() AS base_de_datos")
            result = cursor.fetchone()

        return {
            "mensaje": "Conexión exitosa a MySQL",
            "base_de_datos": result["base_de_datos"]
        }

    finally:
        connection.close()