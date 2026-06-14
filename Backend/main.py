from fastapi import FastAPI

app = FastAPI()

@app.get("/Health")
def home():
    return {"mensaje": "Todo bien pa"}