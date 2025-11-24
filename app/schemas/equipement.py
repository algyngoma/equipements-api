from pydantic import BaseModel

class Equipement(BaseModel):
    id: int
    nom: str
    categorie: str
