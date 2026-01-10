# 🆘 PROMPT DE SECOURS - Pour Continuer une Conversation Bloquée

## 📋 Contexte
Si votre conversation avec l'assistant IA se bloque ou si vous perdez le fil, utilisez ce prompt pour redémarrer intelligemment.

---

## 🔄 PROMPT À COPIER-COLLER

```
Voici l'historique de notre conversation jusqu'à présent :

[COLLEZ ICI VOTRE HISTORIQUE - Exemple ci-dessous]

Question 1 : Décrivez votre projet
Réponse : Je veux créer une app pour mon restaurant

Question 2 : Quelles fonctionnalités principales ?
Réponse : Réservation de tables et menu en ligne

Question 3 : Quel est votre budget ?
Réponse : Environ 5000€

[FIN DE L'HISTORIQUE]

---

Mission : Continue à m'aider à définir mon projet en :
1. Analysant ce que j'ai déjà dit
2. Identifiant les informations manquantes critiques
3. Me posant UNE question précise et pertinente à la fois
4. M'aidant avec des exemples concrets si je suis vague

Aspects encore à explorer (adapte selon ce qui manque dans mon historique) :
- Public cible exact (âge, profil, comportement)
- Pays d'exploitation (important pour la réglementation)
- Secteur d'activité précis
- Délais souhaités
- Équipe disponible et compétences
- Contraintes techniques existantes
- Besoins en sécurité et données sensibles
- Intégrations tierces nécessaires (paiement, email, SMS, etc.)
- Langues supportées
- Accessibilité requise
- Type d'hébergement préféré

Commence par me poser LA prochaine question la plus importante.
```

---

## 🎯 PROMPT POUR GÉNÉRER LE PROMPT FINAL (si vous avez assez d'infos)

```
J'ai terminé de définir mon projet. Voici TOUTES les informations collectées :

[COLLEZ TOUT VOTRE HISTORIQUE ICI]

---

Génère maintenant un PROMPT OPTIMISÉ ULTRA-COMPLET en Markdown qui couvre TOUS les aspects du projet.

Le prompt DOIT inclure ces 12 sections avec du contenu DÉTAILLÉ et CONCRET basé sur mes réponses :

# 🎯 PROMPT OPTIMISÉ - [Titre du projet]

## A. DESCRIPTION DU PROJET
- Objectif principal détaillé (2-3 phrases)
- Fonctionnalités principales (liste concrète)
- Public cible (personas détaillés)
- Contexte et besoin métier (pourquoi ce projet existe)

## B. CONTRAINTES ET RESSOURCES
- Budget exact ou fourchette
- Délais et timeline
- Équipe disponible et compétences
- Contraintes techniques existantes

## C. SÉCURITÉ ET PROTECTION DES DONNÉES
- Mesures de sécurité techniques obligatoires :
  * Chiffrement AES-256
  * Authentification (OAuth 2.0 / JWT)
  * HTTPS/SSL
  * Sauvegardes automatiques
  * Tests de pénétration
- Protection des données personnelles :
  * Minimisation des données
  * Durée de conservation
  * Droits utilisateurs (accès, rectification, suppression)
- Conformité RGPD si Europe :
  * Registre des traitements
  * AIPD si nécessaire
  * DPO si requis
  * Consentement explicite

## D. RÉGLEMENTATION ET CONFORMITÉ
- Réglementations applicables (basées sur mon pays/secteur) :
  * Si France : RGPD, CNIL, lois sectorielles
  * Si e-commerce : DSP2, droit de rétractation, CGV
  * Si santé : HDS, secret médical
  * etc.
- Documents légaux obligatoires (mentions légales, CGU, CGV, cookies)
- Licences et propriété intellectuelle

## E. ÉTHIQUE ET IMPACT SOCIÉTAL
- Accessibilité WCAG 2.1 niveau AA minimum :
  * Contrastes 4.5:1
  * Navigation clavier
  * Textes alternatifs
  * Compatible lecteurs d'écran
- Non-discrimination et équité
- Impact environnemental (éco-conception, hébergeur vert)
- Transparence sur les données et algorithmes

## F. FAISABILITÉ TECHNIQUE
- Stack technique recommandée (justifiée) :
  * Frontend : [React/Vue/Svelte + pourquoi]
  * Backend : [Node.js/Python/PHP + framework]
  * Base de données : [PostgreSQL/MongoDB + justification]
  * Hébergement : [Vercel/OVH/AWS + selon budget/RGPD]
- Architecture système (schéma textuel)
- APIs et services tiers recommandés :
  * Paiement : [Stripe/PayPal + raison]
  * Email : [SendGrid/Brevo]
  * Stockage : [Cloudinary/S3]
  * etc.
- Compatibilité (navigateurs, mobile, PWA)
- Scalabilité et performance

## G. RISQUES ET CONTINGENCES
- Risques techniques (pannes, bugs, performance)
- Risques sécurité (cyberattaques, fuites de données)
- Risques juridiques (non-conformité RGPD)
- Risques financiers (dépassement budget, coûts cachés)
- Plans de mitigation pour chaque risque
- Solutions de repli (plan B)

## H. COMMUNICATION ET ADOPTION
- Stratégie de lancement (marketing, canaux)
- Communication utilisateurs (onboarding, tutoriels)
- Support client (chatbot, email, téléphone)
- Mesure de l'adoption (KPIs, NPS, rétention)

## I. INTERNATIONALISATION
- Langues supportées
- Adaptation culturelle (dates, devises, formats)
- Réglementations locales par pays ciblé

## J. DURABILITÉ ET MAINTENANCE
- Documentation technique complète
- Tests automatisés (coverage > 80%)
- CI/CD pipeline
- Monitoring et alertes
- Plan de fin de vie (archivage, export données)

## K. INDICATEURS DE RÉUSSITE (KPIs)
- KPIs Business (acquisition, conversion, revenue, ROI)
- KPIs Produit (engagement, rétention, satisfaction NPS)
- KPIs Techniques (performance, uptime, bugs)
- Coûts mensuels estimés détaillés :
  * Hébergement : X-Y €/mois
  * APIs : X-Y €/mois
  * Maintenance : X-Y €/mois
  * TOTAL : X-Y €/mois
- ROI attendu et délai de rentabilité

## L. COLLABORATION ET ORGANISATION
- Équipe recommandée (rôles précis) :
  * MVP : 1 dev full-stack, 1 designer, 1 PO
  * Complet : détailler selon projet
- Méthodologie (Agile/Scrum, sprints 2 semaines)
- Outils collaboratifs (GitHub, Trello, Slack, Figma)
- Rôles et responsabilités clairs

## ✅ CHECKLIST DE DÉMARRAGE (30 jours)
Détaille semaine par semaine :
- Semaine 1 : Préparation (MVP, équipe, stack, audit RGPD)
- Semaine 2 : Design (wireframes, maquettes, architecture)
- Semaine 3-4 : Développement MVP
- Semaine 5 : Tests et corrections
- Lancement : déploiement, monitoring, communication

---

**Instructions importantes :**
- Utilise mes informations PRÉCISES de la conversation
- Si une info manque, écris "À définir avec le client"
- Sois CONCRET : nomme des technologies, outils, chiffres réels
- Ajoute des exemples pratiques
- Le prompt doit être ACTIONNABLE immédiatement par une équipe technique

**Date de génération : [Date actuelle]**
```

---

## 💡 PROMPT POUR APPROFONDIR UN ASPECT SPÉCIFIQUE

Si vous voulez approfondir seulement une partie (ex: sécurité, budget, technique) :

```
Voici mon projet en résumé :
[RÉSUMÉ RAPIDE DE VOTRE PROJET EN 3-5 LIGNES]

J'ai besoin d'approfondir spécifiquement l'aspect : [SÉCURITÉ / BUDGET / TECHNIQUE / JURIDIQUE / etc.]

Pose-moi 5 questions précises et pertinentes pour explorer cet aspect en profondeur.

Ensuite, génère une section ultra-détaillée sur ce sujet avec :
- Recommandations concrètes
- Outils et technologies spécifiques
- Checklist actionnable
- Risques et solutions
- Coûts estimés si applicable

Commence par me poser la première question sur ce sujet.
```

---

## 🔧 PROMPT POUR DÉBLOQUER UNE CONVERSATION VAGUE

Si l'IA ou vous êtes trop vagues :

```
Je vais être plus précis sur mon projet. Voici EXACTEMENT ce que je veux :

**Type de projet :** [Application mobile / Site web / SaaS / E-commerce / etc.]

**Problème à résoudre :** [Décris le problème exact en 2 phrases]

**Solution envisagée :** [Comment ton projet résout ce problème]

**Utilisateurs finaux :** [Qui va utiliser ton app/site ? Sois précis : âge, métier, localisation]

**Exemple concret d'utilisation :** 
[Décris un scénario : "Marie, 35 ans, restauratrice, ouvre mon app pour..."]

**Ce que je ne veux PAS :** [Fonctionnalités ou approches à éviter]

Maintenant, avec ces informations précises, aide-moi à structurer le reste du projet en posant des questions ciblées.
```

---

## 📞 PROMPT POUR OBTENIR DE L'AIDE SUR UN PROBLÈME TECHNIQUE SPÉCIFIQUE

```
J'ai un projet défini mais je bloque sur un aspect technique précis :

**Mon projet :** [Description courte]

**Mon problème technique :** 
[Ex: "Je ne sais pas quelle base de données choisir" / "Comment gérer les paiements en toute sécurité" / "Quelle stack pour une app mobile cross-platform"]

**Mes contraintes :**
- Budget : [X €]
- Compétences équipe : [Ex: "Je connais JavaScript mais pas Python"]
- Délai : [X mois]
- Autre : [...]

Recommande-moi :
1. La meilleure solution technique pour mon cas (justifiée)
2. 2-3 alternatives avec avantages/inconvénients
3. Les outils et ressources concrètes à utiliser
4. Un tutoriel ou documentation pour démarrer
5. Les pièges à éviter
```

---

## 🎯 UTILISATION DE CES PROMPTS

1. **Copier** le prompt adapté à votre situation
2. **Remplacer** les sections [ENTRE CROCHETS] par vos vraies infos
3. **Coller** dans l'interface de chat ou le terminal
4. **Suivre** les recommandations de l'IA

---

## 💾 SAUVEGARDEZ CE FICHIER !

Gardez ce fichier `prompt_secours.md` sous la main pour :
- ✅ Redémarrer une conversation bloquée
- ✅ Approfondir un aspect spécifique
- ✅ Générer le prompt final si vous avez toutes les infos
- ✅ Obtenir de l'aide technique ciblée

**Bonne chance avec vos projets ! 🚀**