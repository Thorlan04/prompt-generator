from questionnaire import Questionnaire
from recherche import RechercheurInfos
from generateur import GenerateurPrompt

def main():
    """Programme principal"""
    
    # Étape 1 : Poser les questions
    questionnaire = Questionnaire()
    reponses = questionnaire.poser_questions_terminal()
    
    # Afficher le résumé
    questionnaire.afficher_resume(reponses)
    
    # Étape 2 : Rechercher les réglementations
    print("\n🔍 Recherche des réglementations applicables...")
    rechercheur = RechercheurInfos()
    
    pays = reponses.get('question_3', 'France')
    secteur = reponses.get('question_4', 'general')
    
    reglementations = rechercheur.chercher_reglementation(pays, secteur)
    
    print(f"✅ {len(reglementations)} réglementations identifiées")
    
    # Étape 3 : Générer le prompt
    print("\n⚙️ Génération du prompt optimisé...")
    generateur = GenerateurPrompt()
    prompt_final = generateur.generer(reponses, reglementations)
    
    # Étape 4 : Sauvegarder le résultat
    nom_fichier = "prompt_optimise.md"
    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(prompt_final)
    
    print(f"\n✅ Prompt généré avec succès !")
    print(f"📄 Fichier sauvegardé : {nom_fichier}")
    print("\n" + "=" * 60)
    print("Vous pouvez maintenant ouvrir ce fichier et l'utiliser !")
    print("=" * 60)

if __name__ == "__main__":
    main()