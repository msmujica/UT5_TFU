from fastapi import FastAPI

app = FastAPI()

@app.get("/Health")
def home():
    return {"mensaje": "Todo bien pa"}

@app.get("/db-test")
def db_test(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT DATABASE();"))
    database_name = result.scalar()

    return {
        "mensaje": "Conexión exitosa a MySQL",
        "base_de_datos": database_name
    }