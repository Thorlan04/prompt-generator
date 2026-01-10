from typing import Dict

class Questionnaire:
    """Gère les questions à poser à l'utilisateur"""
    
    def __init__(self):
        self.questions_base = [
            "Quel est l'objectif principal de votre projet ?",
            "Qui sont les utilisateurs finaux ?",
            "Dans quel pays sera utilisé ce projet ?",
            "Quel est votre secteur d'activité ?",
            "Quel est votre budget approximatif (en €) ?"
        ]
    
    def poser_questions_terminal(self) -> Dict[str, str]:
        """Pose les questions en mode terminal"""
        print("\n🎯 Bienvenue dans le générateur de prompts optimaux !")
        print("=" * 60)
        
        reponses = {}
        
        for i, question in enumerate(self.questions_base, 1):
            reponse = input(f"\n{i}. {question}\n   → ")
            reponses[f"question_{i}"] = reponse
        
        return reponses
    
    def afficher_resume(self, reponses: Dict[str, str]):
        """Affiche un résumé des réponses"""
        print("\n" + "=" * 60)
        print("📋 RÉSUMÉ DE VOTRE PROJET")
        print("=" * 60)
        
        for cle, valeur in reponses.items():
            print(f"• {valeur}")