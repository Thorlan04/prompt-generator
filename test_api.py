import os
from dotenv import load_dotenv
from groq import Groq

# Charger .env
load_dotenv()

# Récupérer la clé
api_key = os.getenv("GROQ_API_KEY")

print("=" * 60)
print("DIAGNOSTIC GROQ API")
print("=" * 60)

# Test 1 : Clé chargée ?
print(f"\n1. Clé chargée : {'OUI' if api_key else 'NON'}")
if api_key:
    print(f"   Début : {api_key[:10]}...")
    print(f"   Longueur : {len(api_key)} caractères")
    print(f"   Type : {type(api_key)}")
    
    # Vérifier les espaces
    if api_key != api_key.strip():
        print("   ⚠️ ATTENTION : Espaces détectés !")
        api_key = api_key.strip()
        print(f"   Après nettoyage : {api_key[:10]}...")

# Test 2 : Connexion Groq
print("\n2. Test connexion Groq...")
try:
    client = Groq(api_key=api_key)
    print("   ✅ Client Groq créé")
    
    # Test 3 : Appel API simple
    print("\n3. Test appel API...")
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": "Réponds juste 'TEST OK'"}
        ],
        max_tokens=10
    )
    
    print("   ✅ Appel API réussi !")
    print(f"   Réponse : {response.choices[0].message.content}")
    print("\n" + "=" * 60)
    print("✅ TOUT FONCTIONNE CORRECTEMENT")
    print("=" * 60)
    
except Exception as e:
    print(f"   ❌ ERREUR : {e}")
    print("\n" + "=" * 60)
    print("❌ PROBLÈME DÉTECTÉ")
    print("=" * 60)