import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime

# Configuration de la page
st.set_page_config(
    page_title="Générateur de Prompts IA",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .chat-message.user {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    .chat-message.assistant {
        background-color: #f3e5f5;
        border-left: 4px solid #9c27b0;
    }
    .chat-icon {
        font-size: 1.5rem;
        margin-bottom: 0.5rem;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Charger les variables d'environnement
load_dotenv()

# Initialiser la session
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'historique_conversation' not in st.session_state:
    st.session_state.historique_conversation = []
if 'conversation_terminee' not in st.session_state:
    st.session_state.conversation_terminee = False

# CORRECTION : Toujours recharger la clé API
api_key = os.getenv("GROQ_API_KEY")
if api_key:
    # Nettoyer la clé (enlever espaces, retours à la ligne)
    api_key = api_key.strip()
    try:
        st.session_state.groq_client = Groq(api_key=api_key)
        st.session_state.api_key_valid = True
    except Exception as e:
        st.session_state.groq_client = None
        st.session_state.api_key_valid = False
        st.session_state.api_error = str(e)
else:
    st.session_state.groq_client = None
    st.session_state.api_key_valid = False

def afficher_message(role, content):
    """Affiche un message dans le chat"""
    icon = "👤 Vous" if role == "user" else "🤖 Assistant"
    css_class = "user" if role == "user" else "assistant"
    
    st.markdown(f"""
        <div class="chat-message {css_class}">
            <div class="chat-icon">{icon}</div>
            <div>{content}</div>
        </div>
    """, unsafe_allow_html=True)

def poser_question_intelligente(historique, derniere_reponse=None):
    """Utilise Groq pour générer la prochaine question"""
    
    if not st.session_state.groq_client:
        return "❌ Erreur : Clé API Groq non configurée."
    
    if not historique:
        prompt_systeme = """Tu es un consultant expert qui aide les clients à définir leurs projets digitaux.

Ton rôle :
- Poser UNE SEULE question précise à la fois
- Adapter tes questions aux réponses précédentes
- Proposer des exemples concrets si le client est vague
- Explorer : objectifs, public, budget, délais, compétences, sécurité

Aspects à couvrir :
- Objectif et fonctionnalités principales
- Public cible précis
- Pays d'exploitation (réglementation)
- Secteur d'activité
- Budget et délais
- Équipe disponible et compétences
- Besoins spéciaux (accessibilité, langues, etc.)
- Données sensibles à protéger
- Intégrations nécessaires (paiement, email, etc.)

Après 10+ échanges approfondis, propose la validation.

Réponds UNIQUEMENT avec ta question, sans préambule."""
        
        message = "Le client démarre. Pose-lui la première question pour comprendre son projet."
    else:
        historique_texte = ""
        for i, echange in enumerate(historique, 1):
            historique_texte += f"\n{i}. Q: {echange['question']}\n   R: {echange['reponse']}\n"
        
        prompt_systeme = "Tu es un consultant expert. Continue à approfondir le projet avec des questions pertinentes."
        message = f"""Historique :
{historique_texte}

Dernière réponse : {derniere_reponse}

Pose la prochaine question importante. Si tu as 10+ échanges approfondis, propose : "Je pense avoir assez d'informations. Cliquez sur 'Générer le Prompt' ou continuons."
"""
    
    try:
        response = st.session_state.groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": prompt_systeme},
                {"role": "user", "content": message}
            ],
            temperature=0.7,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Erreur API : {str(e)}"

def generer_prompt_final(historique):
    """Génère le prompt optimisé final"""
    
    historique_texte = ""
    for i, echange in enumerate(historique, 1):
        historique_texte += f"\n{i}. Question : {echange['question']}\n   Réponse : {echange['reponse']}\n"
    
    prompt_generation = f"""Voici la conversation complète avec le client :

{historique_texte}

Génère un PROMPT OPTIMISÉ ULTRA-COMPLET en Markdown avec TOUTES ces sections détaillées :

# 🎯 PROMPT OPTIMISÉ - [Titre du projet]

## A. DESCRIPTION DU PROJET
- Objectif principal détaillé (2-3 phrases)
- Fonctionnalités principales (liste concrète basée sur la conversation)
- Public cible (personas détaillés)
- Contexte métier (pourquoi ce projet existe)

## B. CONTRAINTES ET RESSOURCES
- Budget : [montant exact ou fourchette mentionnée]
- Délais : [timeline mentionnée]
- Équipe disponible : [compétences mentionnées]
- Contraintes techniques : [infrastructure existante ou "from scratch"]

## C. SÉCURITÉ ET PROTECTION DES DONNÉES
### Mesures de sécurité obligatoires :
- Chiffrement AES-256 pour données sensibles
- Authentification sécurisée (OAuth 2.0 ou JWT)
- HTTPS/SSL obligatoire
- Sauvegardes automatiques quotidiennes
- Tests de pénétration avant production

### Protection des données personnelles :
- Minimisation : collecter uniquement le nécessaire
- Durée de conservation limitée et documentée
- Droits utilisateurs : accès, rectification, suppression
- Chiffrement des données en base

### Conformité RGPD (si applicable) :
- Registre des traitements
- AIPD si traitement à risque
- DPO si nécessaire
- Consentement explicite

## D. RÉGLEMENTATION ET CONFORMITÉ
### Réglementations applicables :
[Liste basée sur le pays et secteur mentionnés dans la conversation]

Exemples selon contexte :
- France général : RGPD, CNIL
- E-commerce France : RGPD, DSP2, droit rétractation 14j, CGV obligatoires
- Santé France : RGPD, HDS, secret médical
- Finance : RGPD, DSP2, MIF II, ACPR

### Documents légaux obligatoires :
- Mentions légales
- Politique de confidentialité
- CGU (Conditions Générales d'Utilisation)
- CGV si e-commerce
- Politique cookies

## E. ÉTHIQUE ET IMPACT SOCIÉTAL
### Accessibilité (WCAG 2.1 niveau AA) :
- Contrastes couleurs ≥ 4.5:1
- Navigation clavier complète
- Textes alternatifs images
- Compatible lecteurs d'écran

### Équité :
- Pas de discrimination (origine, genre, âge)
- Audit biais algorithmiques si IA
- Langage inclusif

### Environnement :
- Éco-conception du code
- Hébergeur "vert" si possible
- Optimisation images et médias

## F. FAISABILITÉ TECHNIQUE
### Stack recommandée (justifiée selon projet) :

**Frontend :**
- Framework : React / Vue.js / Svelte [choisir selon complexité]
- UI : Tailwind CSS / Material-UI
- State : Context API / Redux si complexe

**Backend :**
- Framework : Node.js + Express / Python + FastAPI / PHP + Laravel
- API : REST ou GraphQL
- Auth : JWT / OAuth 2.0

**Base de données :**
- Type : PostgreSQL (relationnel) / MongoDB (NoSQL)
- ORM : Prisma / TypeORM / Mongoose
- Cache : Redis si nécessaire

**Hébergement recommandé :**
[Adapter selon pays/budget mentionné]
- Frontend : Vercel / Netlify (gratuit)
- Backend : Railway / Render / OVH (selon RGPD)
- DB : Provider du backend ou séparé
- CDN : Cloudflare (gratuit)

**APIs tierces recommandées :**
[Selon besoins mentionnés]
- Paiement : Stripe / PayPal / Mollie
- Email : SendGrid (100/jour gratuit) / Brevo
- SMS : Twilio
- Stockage fichiers : Cloudinary / AWS S3

### Architecture :
[Schéma textuel : Client → CDN → API → DB]

### Compatibilité :
- Responsive (mobile-first)
- Navigateurs : Chrome, Firefox, Safari, Edge (2 dernières versions)
- PWA si mobile important

## G. RISQUES ET CONTINGENCES
### Risques techniques :
1. Pannes serveur → Monitoring 24/7, backup serveur
2. Bugs critiques → Tests auto >80%, rollback
3. Performance → Load testing, CDN, caching

### Risques sécurité :
1. Cyberattaques → Audit sécu, WAF, assurance cyber
2. Fuites données → Chiffrement, accès limités, protocole RGPD

### Risques juridiques :
1. Non-conformité RGPD → Audit juridique pré-lancement

### Risques financiers :
1. Dépassement budget → Tampon 20%, suivi hebdo
2. Coûts cachés → Calcul précis avec marge

## H. COMMUNICATION ET ADOPTION
### Lancement :
- Phase bêta : 10-50 testeurs
- Marketing : [canaux selon public cible]
- Incentives : [offres lancement]

### Support :
- Onboarding emails (série de 5)
- Tutoriels vidéo
- FAQ complète
- Support : chatbot + email

### KPIs adoption :
- Inscriptions / téléchargements
- Rétention 7/30/90 jours
- NPS > 50

## I. INTERNATIONALISATION
### Langues :
[Selon conversation ou "Français uniquement au lancement"]

### Implémentation :
- Bibliothèque i18n appropriée
- Traduction professionnelle
- Adaptation culturelle (dates, devises, formats)

## J. DURABILITÉ ET MAINTENANCE
### Documentation :
- README complet
- Documentation technique (Wiki)
- Guide contribution

### Tests :
- Tests unitaires
- Tests intégration
- Tests e2e
- Coverage > 80%

### CI/CD :
- GitHub Actions / GitLab CI
- Déploiement automatique
- Versioning sémantique

### Monitoring :
- Uptime (UptimeRobot)
- Erreurs (Sentry)
- Analytics (Plausible - RGPD)
- Performance (Lighthouse CI)

## K. INDICATEURS DE RÉUSSITE (KPIs)
### KPIs Business :
- Acquisition : [objectif X users/mois]
- Conversion : [taux objectif X%]
- Revenue : [CA objectif si applicable]
- ROI : [retour attendu sous X mois]

### KPIs Produit :
- Engagement : temps session > X min
- Rétention : X% actifs après 30j
- Satisfaction : NPS > 50

### KPIs Techniques :
- Performance : Lighthouse > 90
- Uptime : > 99.5%
- Bugs critiques : < 5/mois

### Coûts mensuels estimés :
- Hébergement : X-Y €
- APIs : X-Y €
- Maintenance : X-Y €
- **TOTAL : X-Y €/mois**

## L. COLLABORATION ET ORGANISATION
### Équipe recommandée :
**MVP :**
- 1 Product Owner
- 1 Dev Full-Stack (ou 1 Front + 1 Back)
- 1 Designer UX/UI (freelance OK)

**Complet :**
[Adapter selon taille projet]

### Méthodologie :
- Agile / Scrum
- Sprints 2 semaines
- Stand-ups quotidiens 15min

### Outils :
- Code : GitHub / GitLab
- Projet : Trello / Notion / Jira
- Communication : Slack / Discord
- Design : Figma
- Docs : Notion / Confluence

## ✅ CHECKLIST DE DÉMARRAGE (30 jours)

### Semaine 1 : Préparation
- [ ] Définir MVP (fonctionnalités essentielles)
- [ ] Valider budget et timeline
- [ ] Constituer équipe
- [ ] Étude concurrence rapide
- [ ] Audit RGPD initial
- [ ] Choisir stack technique

### Semaine 2 : Design & Architecture
- [ ] Wireframes
- [ ] Maquettes haute fidélité
- [ ] Architecture technique validée
- [ ] Choix providers (hosting, APIs)
- [ ] Setup environnements (dev, staging, prod)

### Semaine 3-4 : Développement MVP
- [ ] Backend : API endpoints essentiels
- [ ] Frontend : écrans principaux
- [ ] Intégrations tierces
- [ ] Tests unitaires
- [ ] Documentation

### Semaine 5 : Tests & Corrections
- [ ] Tests utilisateurs bêta (10-20 personnes)
- [ ] Corrections bugs critiques
- [ ] Tests sécurité
- [ ] Optimisation performances
- [ ] Validation RGPD finale

### Lancement :
- [ ] Déploiement production
- [ ] Monitoring activé
- [ ] Communication lancement
- [ ] Support opérationnel

---

**🚀 Ce prompt est COMPLET et ACTIONNABLE !**

Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M')}
Par Générateur de Prompts IA - Propulsé par Groq
"""

    try:
        response = st.session_state.groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt_generation}
            ],
            temperature=0.7,
            max_tokens=4000
        )
        
        prompt_final = response.choices[0].message.content.strip()
        
        # Sauvegarder
        nom_fichier = f"prompt_optimise_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        with open(nom_fichier, "w", encoding="utf-8") as f:
            f.write(prompt_final)
        
        return prompt_final, nom_fichier
    except Exception as e:
        return f"❌ Erreur : {str(e)}", None

# ==================== INTERFACE PRINCIPALE ====================

# Header
st.title("🚀 Générateur de Prompts IA Optimaux")
st.markdown("**Propulsé par Groq (Llama 3.3) - 100% Gratuit**")
st.divider()

# Sidebar
with st.sidebar:
    st.header("📊 Tableau de bord")
    
    if st.session_state.groq_client and st.session_state.get('api_key_valid', False):
        st.success("✅ API Groq connectée")
    else:
        st.error("❌ API non configurée")
        if st.session_state.get('api_error'):
            st.warning(f"⚠️ Erreur : {st.session_state.api_error}")
        st.info("Vérifiez GROQ_API_KEY dans .env")
    
    st.divider()
    
    # Statistiques
    nb_questions = len(st.session_state.historique_conversation)
    st.metric("📝 Questions posées", nb_questions)
    
    if nb_questions >= 10:
        st.success("✅ Informations suffisantes")
    elif nb_questions >= 5:
        st.warning(f"⏳ {10 - nb_questions} questions recommandées")
    else:
        st.info(f"💡 {10 - nb_questions} questions minimum")
    
    st.divider()
    
    # Commandes
    st.subheader("💡 Guide")
    st.markdown("""
    **Utilisation :**
    1. Répondez aux questions
    2. Soyez précis (mais OK si vague)
    3. Minimum 5 questions
    4. Cliquez "Générer" quand prêt
    """)
    
    st.divider()
    
    # Boutons d'action
    if st.button("🔄 Nouvelle conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.historique_conversation = []
        st.session_state.conversation_terminee = False
        st.rerun()
    
    if st.session_state.historique_conversation and not st.session_state.conversation_terminee:
        if st.button("📋 Voir le résumé", use_container_width=True):
            st.session_state.show_resume = True
            st.rerun()

# Afficher le résumé si demandé
if hasattr(st.session_state, 'show_resume') and st.session_state.show_resume:
    with st.expander("📋 Résumé de vos réponses", expanded=True):
        for i, echange in enumerate(st.session_state.historique_conversation, 1):
            st.markdown(f"**{i}. {echange['question']}**")
            st.markdown(f"→ {echange['reponse']}")
            st.divider()
        if st.button("Fermer"):
            st.session_state.show_resume = False
            st.rerun()

# Zone principale
if not st.session_state.groq_client:
    st.error("⚠️ Configuration API Groq requise")
    st.info("""
    **Pour démarrer :**
    1. Créez un compte : https://console.groq.com/ (gratuit)
    2. Créez une API Key
    3. Ajoutez dans `.env` : `GROQ_API_KEY=votre_clé`
    4. Relancez l'application
    """)
else:
    # Afficher l'historique
    for message in st.session_state.messages:
        afficher_message(message["role"], message["content"])
    
    # Conversation non démarrée
    if not st.session_state.messages and not st.session_state.conversation_terminee:
        st.info("👋 **Bienvenue !** Cliquez sur 'Démarrer' pour commencer la conversation.")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🎬 Démarrer la conversation", use_container_width=True, type="primary"):
                with st.spinner("Préparation..."):
                    question_initiale = poser_question_intelligente([])
                st.session_state.messages.append({"role": "assistant", "content": question_initiale})
                st.rerun()
    
    # Conversation en cours
    elif not st.session_state.conversation_terminee:
        st.divider()
        
        # Zone de réponse
        # Générer une clé unique basée sur le nombre de messages
        input_key = f"user_input_{len(st.session_state.messages)}"

        user_input = st.text_input(
            "Votre réponse :",
            placeholder="Tapez votre réponse ici...",
            key=input_key
)
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            if st.button("📤 Envoyer", use_container_width=True, type="primary"):
                if user_input:
                    # Ajouter réponse utilisateur
                    st.session_state.messages.append({"role": "user", "content": user_input})
                    
                    # Enregistrer dans l'historique
                    derniere_question = st.session_state.messages[-2]["content"] if len(st.session_state.messages) >= 2 else "Question initiale"
                    st.session_state.historique_conversation.append({
                        "question": derniere_question,
                        "reponse": user_input
                    })
                    
                    # Générer prochaine question
                    with st.spinner("🤔 L'IA réfléchit..."):
                        prochaine_question = poser_question_intelligente(
                            st.session_state.historique_conversation,
                            user_input
                        )
                    st.session_state.messages.append({"role": "assistant", "content": prochaine_question})
                    
                    st.rerun()
                else:
                    st.warning("⚠️ Veuillez entrer une réponse")
        
        with col2:
            if len(st.session_state.historique_conversation) >= 5:
                if st.button("✅ Générer le Prompt", use_container_width=True):
                    st.session_state.conversation_terminee = True
                    st.rerun()
            else:
                st.button("✅ Générer", disabled=True, use_container_width=True, 
                         help=f"Répondez à au moins {5 - len(st.session_state.historique_conversation)} question(s) de plus")
    
    # Génération du prompt
    if st.session_state.conversation_terminee:
        st.success("✅ **Informations collectées !** Génération du prompt en cours...")
        
        with st.spinner("⚙️ Génération (20-30 secondes)..."):
            prompt_final, nom_fichier = generer_prompt_final(st.session_state.historique_conversation)
        
        if nom_fichier:
            st.balloons()
            st.success(f"🎉 **Prompt généré avec succès !**")
            
            # Stats
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("📝 Questions", len(st.session_state.historique_conversation))
            with col2:
                st.metric("📄 Taille", f"{len(prompt_final)} car.")
            with col3:
                st.metric("📋 Sections", "12+")
            
            st.divider()
            
            # Aperçu
            with st.expander("👁️ Aperçu (600 premiers caractères)", expanded=True):
                st.markdown(prompt_final[:600] + "...")
            
            # Téléchargement
            st.download_button(
                label="📥 Télécharger le prompt complet (.md)",
                data=prompt_final,
                file_name=nom_fichier,
                mime="text/markdown",
                use_container_width=True,
                type="primary"
            )
            
            # Prompt complet
            with st.expander("📄 Voir le prompt complet"):
                st.markdown(prompt_final)
            
            st.divider()
            
            # Nouvelle conversation
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("🔄 Créer un nouveau prompt", use_container_width=True):
                    st.session_state.messages = []
                    st.session_state.historique_conversation = []
                    st.session_state.conversation_terminee = False
                    st.rerun()
        else:
            st.error(prompt_final)

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.9rem; padding: 1rem;'>
    <strong>Générateur de Prompts IA</strong> • Propulsé par <strong>Groq</strong> • 100% Gratuit<br>
    Créé avec ❤️ pour vous aider à structurer vos projets digitaux
</div>
""", unsafe_allow_html=True)