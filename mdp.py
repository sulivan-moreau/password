import string
import hashlib
import json

# Condition
def mdp_user():
    while True:
        mdp = input("Entrez votre mot de passe : ")
        if len(mdp) < 8:
            print("Vous devez renseigner un mot de passe d'au moins 8 caractères.")
        elif not any(char.islower() for char in mdp):
            print("Le mot de passe doit contenir au moins une lettre minuscule.")
        elif not any(char.isupper() for char in mdp):
            print("Le mot de passe doit contenir au moins une lettre majuscule.")
        elif not any(char.isdigit() for char in mdp):
            print("Le mot de passe doit contenir au moins un chiffre.")
        elif not any(char in string.punctuation for char in mdp):
            print("Le mot de passe doit contenir au moins un caractère spécial.")
        else:
            return mdp

# Cryptage
def hashed_mdp(mdp):
    hashed_mdp = hashlib.sha256(mdp.encode()).hexdigest()
    return hashed_mdp

# Fonction pour enregistrer un nouveau mot de passe
def enregistrer_mot_de_passe(nom_utilisateur):
    while True:  # Boucle extérieure pour réessayer en cas de collision
        try:
            with open("mots_de_passe.json", "r") as fichier:
                donnees = json.load(fichier)
        except (FileNotFoundError, json.JSONDecodeError):
            donnees = {}

        # Vérifier si l'utilisateur a déjà un mot de passe enregistré
        if nom_utilisateur in donnees and "mot_de_passe" in donnees[nom_utilisateur]:
            print("Un mot de passe est déjà enregistré pour cet utilisateur.")
            choix = input("Voulez-vous enregistrer un nouveau mot de passe ou afficher vos mots de passe existants? (new/view): ").lower()
            if choix == 'new':
                mdp_user()
                
                continue
            elif choix == 'view':
                afficher_mots_de_passe(donnees)
                return False
            else:
                return False
        else:
            mdp_saisi = mdp_user()
            mdp_hache = hashed_mdp(mdp_saisi)

            # Ajouter les données
            donnees.setdefault(nom_utilisateur, {})["mot_de_passe"] = mdp_hache

            with open("mots_de_passe.json", "w") as fichier:
                json.dump(donnees, fichier, indent=4)

            return True

# Fonction pour afficher les mots de passe existants
def afficher_mots_de_passe(donnees):
    print("Mots de passe enregistrés :")
    for utilisateur, info in donnees.items():
        mot_de_passe = info.get("mot_de_passe", "N/A")
        print(f"{utilisateur}: {mot_de_passe}")

# Demander et hasher le mot de passe
nom_utilisateur = input("Entrez votre nom d'utilisateur : ")

# Enregistrer le mot de passe haché dans le fichier JSON ou afficher les mots de passe existants
if enregistrer_mot_de_passe(nom_utilisateur):
    print("Le mot de passe est enregistré")
