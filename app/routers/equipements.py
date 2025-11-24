from fastapi import APIRouter, HTTPException
from app.schemas.equipement import Equipement
from app.database.memory import equipements_db
from app.constants import NOT_FOUND_MSG


router = APIRouter(
    prefix="/equipements",
    tags=["Équipements"]
)

@router.get("/")
def home():
    return {"message": "Hello FastAPI depuis le bootcamp DevOps !"}


# 🔹 GET /equipements → liste complète
@router.get("/")
def get_all():
    return equipements_db


# 🔹 GET /equipements/{id} → un seul élément
@router.get("/{id}")
def get_one(id: int):
    for eq in equipements_db:
        if eq.id == id:
            return eq
    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


# 🔹 POST /equipements → ajouter un élément
@router.post("/")
def create(equipement: Equipement):
    equipements_db.append(equipement)
    return {"message": "Équipement ajouté", "data": equipement}


# 🔹 PUT /equipements/{id} → modifier un élément
@router.put("/{id}")
def update(id: int, payload: Equipement):
    for i, eq in enumerate(equipements_db):
        if eq.id == id:
            equipements_db[i] = payload
            return {"message": "Équipement mis à jour", "data": payload}
    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


# 🔹 DELETE /equipements/{id} → supprimer un élément
@router.delete("/{id}")
def delete(id: int):
    for i, eq in enumerate(equipements_db):
        if eq.id == id:
            equipements_db.pop(i)
            return {"message": "Équipement supprimé"}
    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)

