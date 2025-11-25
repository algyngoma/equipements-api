from app.database.mongo import equipements_collection
from app.models.equipement import EquipementModel
from app.schemas.equipement import Equipement


def create_equipement(data: Equipement):
    equip = EquipementModel(**data.dict())
    equipements_collection.insert_one(equip.to_dict())
    return equip.to_dict()


def list_equipements():
    return list(equipements_collection.find({}, {"_id": 0}))


def get_equipement_by_id(id: int):
    return equipements_collection.find_one({"id": id}, {"_id": 0})


def delete_equipement(id: int):
    return equipements_collection.delete_one({"id": id})
