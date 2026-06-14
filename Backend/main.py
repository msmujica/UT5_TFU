from fastapi import FastAPI

from Database.connection import get_connection

app = FastAPI()


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