from typing import List, Dict

class RechercheurInfos:
    """Recherche des informations réglementaires et techniques"""
    
    def __init__(self):
        # Base de données locale des réglementations
        self.db_reglementations = {
            "France": {
                "general": ["RGPD", "CNIL"],
                "restauration": ["RGPD", "Normes HACCP", "TVA 10%"],
                "sante": ["RGPD", "HIPAA équivalent FR", "HDS (Hébergement Données de Santé)"],
                "ecommerce": ["RGPD", "DSP2 (paiements)", "Directive e-commerce"],
                "finance": ["RGPD", "DSP2", "MIF II", "ACPR"]
            },
            "UE": {
                "general": ["RGPD", "eIDAS", "NIS2"],
                "sante": ["RGPD", "Règlement sur les dispositifs médicaux"],
                "ecommerce": ["RGPD", "DSP2", "Directive sur les droits des consommateurs"]
            }
        }
        
        # APIs et outils recommandés
        self.db_apis = {
            "paiement": ["Stripe", "PayPal", "Mollie (EU)"],
            "email": ["SendGrid (gratuit: 100/jour)", "Mailgun"],
            "sms": ["Twilio", "OVH SMS"],
            "cartes": ["Mapbox", "OpenStreetMap (gratuit)"],
            "stockage": ["AWS S3", "Cloudinary (gratuit)"]
        }
    
    def chercher_reglementation(self, pays: str, secteur: str) -> List[str]:
        """Récupère les réglementations applicables"""
        reglementations = []
        
        # Réglementations générales du pays
        if pays in self.db_reglementations:
            reglementations.extend(
                self.db_reglementations[pays].get("general", [])
            )
            
            # Réglementations spécifiques au secteur
            reglementations.extend(
                self.db_reglementations[pays].get(secteur.lower(), [])
            )
        
        # Dédoublonner
        return list(set(reglementations))
    
    def recommander_apis(self, fonctionnalites: List[str]) -> Dict[str, List[str]]:
        """Recommande des APIs en fonction des besoins"""
        recommandations = {}
        
        for fonc in fonctionnalites:
            fonc_lower = fonc.lower()
            for categorie, apis in self.db_apis.items():
                if categorie in fonc_lower:
                    recommandations[categorie] = apis
        
        return recommandations