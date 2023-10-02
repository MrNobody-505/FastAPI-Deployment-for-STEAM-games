from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#http://127.0.0.1:8000

@app.get("/")

def index():
    return {"Hola! soy César Forero", 
            "e-mail: cesarjf18@hotmail.com"
            "GitHub: MrNobody-505" }
