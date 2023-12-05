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

# Demander et hasher le mot de passe
nom_utilisateur = input("Entrez votre nom d'utilisateur : ")
mdp_saisi = mdp_user()
mdp_hache = hashed_mdp(mdp_saisi)

# Enregistrement du mot de passe dans un fichier JSON
def enregistrer_mot_de_passe(nom_utilisateur, Outils, mdp_hache):
    try:
        with open("mots_de_passe.json", "r") as fichier:
            donnees = json.load(fichier)
    except (FileNotFoundError, json.JSONDecodeError):
        donnees = {}

    # Si l'utilisateur n'existe pas, le créer
    if nom_utilisateur not in donnees:
        donnees[nom_utilisateur] = {}

    # Vérifier si l'outil existe déjà pour cet utilisateur
    if Outils not in donnees[nom_utilisateur]:
        donnees[nom_utilisateur][Outils] = mdp_hache
    else:
        print("Le même outil est déjà enregistré pour cet utilisateur.")
        return False

    with open("mots_de_passe.json", "w") as fichier:
        json.dump(donnees, fichier, indent=4)

    return True

# Enregistrer le mot de passe haché dans le fichier JSON
Outils = input("Entrez l'outil utilisé : ")
while not enregistrer_mot_de_passe(nom_utilisateur, Outils, mdp_hache):
    mdp_saisi = mdp_user()
    mdp_hache = hashed_mdp(mdp_saisi)

# Message de validation
print("Le mot de passe est enregistré")
