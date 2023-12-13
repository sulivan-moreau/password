import string
import hashlib
import json

# Fonction pour saisir le mot de passe de l'utilisateur
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

# Fonction pour hasher le mot de passe
def hashed_mdp(mdp):
    return hashlib.sha256(mdp.encode()).hexdigest()

# Fonction pour enregistrer un nouveau mot de passe
def enregistrer_mot_de_passe(nom_utilisateur):
    try:
        with open("mots_de_passe.json", "r") as fichier:
            donnees = json.load(fichier)
    except (FileNotFoundError, json.JSONDecodeError):
        donnees = {}

    donnees.setdefault(nom_utilisateur, {"mots_de_passe": []})

    while True:
        choix = input("Voulez-vous enregistrer un nouveau mot de passe ou afficher vos mots de passe existants? (nouveau/voir/fin): ").lower()
        if choix == 'nouveau':
            mdp_saisi = mdp_user()
            mdp_hache = hashed_mdp(mdp_saisi)

            if mdp_hache not in donnees[nom_utilisateur]["mots_de_passe"]:
                donnees[nom_utilisateur]["mots_de_passe"].append(mdp_hache)
                print("Nouveau mot de passe enregistré.")
            else:
                print("Ce mot de passe est déjà enregistré pour cet utilisateur.")

        elif choix == 'voir':
            afficher_mots_de_passe(donnees)
        elif choix == 'fin':
            break
        else:
            print("Choix non valide.")

    with open("mots_de_passe.json", "w") as fichier:
        json.dump(donnees, fichier, indent=4)

    return True

# Fonction pour afficher les mots de passe existants
def afficher_mots_de_passe(donnees):
    print("Mots de passe enregistrés :")
    for utilisateur, info in donnees.items():
        mots_de_passe = info.get("mots_de_passe", ["N/A"])
        print(f"{utilisateur}:")
        for mdp in mots_de_passe:
            print(f"  - {mdp}")

# Demander et hasher le mot de passe
nom_utilisateur = input("Entrez votre nom d'utilisateur : ")

# Enregistrer le mot de passe haché dans le fichier JSON ou afficher les mots de passe existants
if enregistrer_mot_de_passe(nom_utilisateur):
    print("Le mot de passe est enregistré")
