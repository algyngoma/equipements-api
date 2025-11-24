from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn




app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI depuis le bootcamp DevOps !"}

@app.get("/equipements")
def search():
    return []


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)