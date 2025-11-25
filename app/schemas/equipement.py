from enum import Enum
from pydantic import BaseModel, IPvAnyAddress, Field
from datetime import datetime, timezone


class CategorieEnum(str, Enum):
    RESEAU = "reseau"
    SERVEUR = "serveur"
    VM = "vm"
    STOCKAGE = "stockage"
    SECURITE = "securite"
    AUTRE = "autre"


class Equipement(BaseModel):
    id: int
    nom: str
    categorie: CategorieEnum
    ip: IPvAnyAddress
    adresse_mac: str
    emplacement: str
    status: str    # up | down | maintenance
    type: str      # server | switch | router | vm | firewall

    date_ajout: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
