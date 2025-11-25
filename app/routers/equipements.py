from fastapi import APIRouter, HTTPException
from app.schemas.equipement import Equipement
from app.services.equipement_service import (
    create_equipement,
    list_equipements,
    get_equipement_by_id,
    delete_equipement
)
from app.constants import NOT_FOUND_MSG

router = APIRouter(
    prefix="/equipements",
    tags=["Équipements"]
)


@router.post("/")
def add_equipment(data: Equipement):
    return create_equipement(data)


@router.get("/")
def get_all():
    return list_equipements()


@router.get("/{id}")
def get_one(id: int):
    equip = get_equipement_by_id(id)
    if not equip:
        raise HTTPException(404, NOT_FOUND_MSG)
    return equip


@router.delete("/{id}")
def remove(id: int):
    result = delete_equipement(id)
    return {"deleted": result.deleted_count}
