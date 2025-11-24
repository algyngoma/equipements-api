from fastapi import FastAPI
from app.routers import equipements

app = FastAPI()

# Inclusion des routers
app.include_router(equipements.router)

@app.get("/")
def home():
    return {"message": "Hello FastAPI depuis l’architecture PRO 🚀"}
