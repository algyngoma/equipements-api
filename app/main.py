from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import equipements

app = FastAPI()

# ----------- CORS -----------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Autorise toutes les origines (React, localhost, Docker…)
    allow_credentials=True,
    allow_methods=["*"],   # Autorise GET, POST, PUT, DELETE...
    allow_headers=["*"],   # Autorise tous les headers
)

# ----------- ROUTERS -------
app.include_router(equipements.router)

@app.get("/")
def home():
    return {"message": "Hello FastAPI depuis l’architecture PRO 🚀"}
