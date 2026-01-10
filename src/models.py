from pydantic import BaseModel
from typing import List, Optional

class ProjetContext(BaseModel):
    """Contexte du projet de l'utilisateur"""
    objectif: str
    public_cible: str = "Grand public"
    pays: str = "France"
    secteur: str
    budget: Optional[float] = None
    delai_mois: Optional[int] = None
    competences: List[str] = []

class PromptOptimise(BaseModel):
    """Structure du prompt généré"""
    description: str
    contraintes: dict
    securite: List[str]
    reglementation: List[str]
    ethique: List[str]
    technique: dict
    risques: List[str]
    kpis: List[str]