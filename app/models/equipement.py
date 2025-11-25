from datetime import datetime, timezone
from typing import Optional

class EquipementModel:
    """
    Modèle interne utilisé juste pour insérer dans MongoDB.
    Il reçoit les objets déjà validés par Pydantic.
    """

    def __init__(
        self,
        id: int,
        nom: str,
        categorie,
        ip,
        adresse_mac: str,
        emplacement: str,
        status: str,
        type: str,
        date_ajout: Optional[datetime] = None
    ):
        self.id = id
        self.nom = nom
        self.categorie = str(categorie)  # on stocke une string dans Mongo
        self.ip = str(ip)                # idem pour l’IP validée
        self.adresse_mac = adresse_mac
        self.emplacement = emplacement
        self.status = status
        self.type = type

        self.date_ajout = date_ajout or datetime.now(timezone.utc)

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "categorie": self.categorie,
            "ip": self.ip,
            "adresse_mac": self.adresse_mac,
            "emplacement": self.emplacement,
            "status": self.status,
            "type": self.type,
            "date_ajout": self.date_ajout
        }
