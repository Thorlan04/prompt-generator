from typing import Dict, List

class GenerateurPrompt:
    """Génère le prompt optimisé final"""
    
    def generer(self, reponses: Dict, reglementations: List[str]) -> str:
        """Génère le prompt structuré en Markdown"""
        
        prompt = f"""# 🎯 PROMPT OPTIMISÉ - PROJET

## A. DESCRIPTION DU PROJET

**Objectif principal :**
{reponses.get('question_1', 'Non renseigné')}

**Public cible :**
{reponses.get('question_2', 'Non renseigné')}

**Pays d'exploitation :**
{reponses.get('question_3', 'Non renseigné')}

**Secteur d'activité :**
{reponses.get('question_4', 'Non renseigné')}

---

## B. CONTRAINTES

**Budget :**
{reponses.get('question_5', 'Non renseigné')} €

---

## C. SÉCURITÉ ET PROTECTION DES DONNÉES

### Mesures de sécurité obligatoires :
- ✅ Chiffrement des données (AES-256)
- ✅ Authentification sécurisée (OAuth 2.0 ou JWT)
- ✅ HTTPS/SSL obligatoire
- ✅ Sauvegardes automatiques quotidiennes
- ✅ Tests de sécurité réguliers

### Protection des données personnelles :
- Collecte minimale des données (principe de minimisation)
- Durée de conservation limitée et documentée
- Droit d'accès, de rectification et de suppression
- Registre des traitements de données

---

## D. RÉGLEMENTATION ET CONFORMITÉ

### Réglementations applicables :
"""
        
        for regle in reglementations:
            prompt += f"- ✅ {regle}\n"
        
        prompt += """
### Points de vigilance :
- Désigner un DPO (Délégué à la Protection des Données) si nécessaire
- Réaliser une AIPD (Analyse d'Impact) pour les traitements à risque
- Obtenir le consentement explicite des utilisateurs
- Prévoir les mentions légales et CGU/CGV

---

## E. ÉTHIQUE ET IMPACT SOCIÉTAL

### Principes éthiques :
- 🌍 Accessibilité (conformité WCAG 2.1 AA minimum)
- ⚖️ Non-discrimination et équité algorithmique
- 🌱 Impact environnemental réduit (éco-conception)
- 🔒 Transparence sur l'utilisation des données

### Actions concrètes :
- Tester l'accessibilité avec des utilisateurs en situation de handicap
- Auditer les biais algorithmiques potentiels
- Choisir un hébergeur "vert" si possible
- Rédiger une charte éthique du projet

---

## F. FAISABILITÉ TECHNIQUE

### Stack technique recommandée :
**Frontend :**
- React ou Vue.js (interfaces modernes)
- Tailwind CSS (design rapide)

**Backend :**
- Node.js + Express (JavaScript)
- OU Python + FastAPI (performances)

**Base de données :**
- PostgreSQL (relationnelle, robuste)
- OU MongoDB (NoSQL, flexible)

**Hébergement :**
- Vercel / Netlify (frontend, gratuit)
- Railway / Render (backend, freemium)
- OVH / Scaleway (données en UE pour RGPD)

### Compatibilité :
- ✅ Responsive design (mobile, tablette, desktop)
- ✅ Navigateurs : Chrome, Firefox, Safari, Edge (2 dernières versions)
- ✅ Progressive Web App (PWA) pour installation mobile

---

## G. RISQUES ET CONTINGENCES

### Risques identifiés :
1. **Technique :** Pannes serveur, bugs critiques
   - ➡️ Plan : Monitoring 24/7, serveur de secours
   
2. **Sécurité :** Cyberattaques, fuites de données
   - ➡️ Plan : Audit de sécurité, assurance cyber
   
3. **Juridique :** Non-conformité RGPD
   - ➡️ Plan : Audit juridique avant mise en production
   
4. **Financier :** Dépassement de budget
   - ➡️ Plan : Budget tampon de 20%, phase MVP d'abord

---

## H. COMMUNICATION ET ADOPTION

### Stratégie de lancement :
- 📢 Campagne sur les réseaux sociaux (LinkedIn, Instagram)
- 📧 Email marketing ciblé
- 🎓 Tutoriels vidéo et documentation claire
- 💬 Support client réactif (chatbot + email)

### Mesure de l'adoption :
- Nombre d'inscriptions / téléchargements
- Taux de rétention (utilisateurs actifs après 30 jours)
- NPS (Net Promoter Score)

---

## I. INTERNATIONALISATION

### Préparation :
- 🌐 Interface multilingue (i18n)
- 💱 Gestion multi-devises si applicable
- 📝 Adaptation des mentions légales par pays

---

## J. DURABILITÉ

### Pérennité technique :
- Documentation complète du code
- Tests automatisés (couverture > 80%)
- Mises à jour de sécurité mensuelles

### Fin de vie :
- Plan d'archivage des données (7 ans minimum pour factures)
- Export des données utilisateurs en format ouvert
- Communication 6 mois avant fermeture

---

## K. INDICATEURS DE RÉUSSITE (KPIs)

### KPIs prioritaires :
1. **Acquisition :** Nombre d'utilisateurs actifs mensuels (objectif: +20%/mois)
2. **Engagement :** Temps moyen passé sur l'application
3. **Satisfaction :** Score NPS > 50
4. **Financier :** ROI (Retour sur Investissement)
5. **Technique :** Disponibilité du service > 99.5%

### Coûts à anticiper :
- Hébergement : ~50-200 €/mois
- Maintenance : 10-20% du coût de développement/an
- Support client : ~1 ETP (Équivalent Temps Plein) si +1000 utilisateurs

---

## L. COLLABORATION ET ORGANISATION

### Équipe recommandée :
- 1 Chef de projet / Product Owner
- 1-2 Développeurs (full-stack ou front+back)
- 1 Designer UX/UI
- 1 Expert sécurité/juridique (conseil externe OK)

### Outils collaboratifs :
- 💻 GitHub / GitLab (code)
- 📋 Trello / Notion (gestion de projet)
- 💬 Slack / Discord (communication)
- 🎨 Figma (design)

---

## ✅ CHECKLIST DE DÉMARRAGE

- [ ] Définir le MVP (Minimum Viable Product)
- [ ] Choisir la stack technique
- [ ] Constituer l'équipe
- [ ] Réaliser une étude de marché rapide
- [ ] Vérifier la conformité RGPD
- [ ] Créer les wireframes / maquettes
- [ ] Développer le MVP
- [ ] Tester avec des utilisateurs bêta
- [ ] Corriger les bugs critiques
- [ ] Lancer en version 1.0
- [ ] Collecter les retours et itérer

---

**🚀 Ce prompt est prêt à être utilisé par une IA ou une équipe de développement !**
"""
        
        return prompt