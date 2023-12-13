import string
import hashlib
import json
import random

# Fonction pour générer un mot de passe aléatoire
def generer_mdp_aleatoire(longueur=12):
    caractere = string.ascii_letters + string.digits + string.punctuation
    while True:
        mdp = ''.join(random.choice(caractere) for i in range(longueur))
        if (any(char.islower() for char in mdp) and
                any(char.isupper() for char in mdp) and
                any(char.isdigit() for char in mdp) and
                any(char in string.punctuation for char in mdp)):
            break
    return mdp

# Fonction pour demander à l'utilisateur de saisir un mot de passe
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
def enregistrer_mot_de_passe(nom_utilisateur, mdp_saisi):
    try:
        with open("mots_de_passe.json", "r") as fichier:
            donnees = json.load(fichier)
    except (FileNotFoundError, json.JSONDecodeError):
        donnees = {}

    donnees.setdefault(nom_utilisateur, {"mots_de_passe": []})
    mdp_hache = hashed_mdp(mdp_saisi)

    if mdp_hache in donnees[nom_utilisateur]["mots_de_passe"]:
        print("Ce mot de passe est déjà utilisé.")
        return False

    donnees[nom_utilisateur]["mots_de_passe"].append(mdp_hache)
    with open("mots_de_passe.json", "w") as fichier:
        json.dump(donnees, fichier, indent=4)

    return True

# Fonction pour afficher les mots de passe existants
def afficher_mots_de_passe(donnees):
    print("Mots de passe enregistrés :")
    for utilisateur, info in donnees.items():
        print(f"{utilisateur}:")
        for mdp in info.get("mots_de_passe", ["N/A"]):
            print(f"  - {mdp}")

# Programme principal
def main():
    nom_utilisateur = input("Entrez votre nom d'utilisateur : ")

    while True:
        choix = input("Souhaitez-vous générer un mot de passe aléatoire, créer le vôtre, voir les mots de passe existants ou quitter? (générer/créer/voir/quitter): ").lower()
        if choix == 'générer':
            mdp_genere = generer_mdp_aleatoire()
            print(f"Mot de passe généré : {mdp_genere}")
            if enregistrer_mot_de_passe(nom_utilisateur, mdp_genere):
                print("Le mot de passe est enregistré")
        elif choix == 'créer':
            mdp_saisi = mdp_user()
            if enregistrer_mot_de_passe(nom_utilisateur, mdp_saisi):
                print("Le mot de passe est enregistré")
        elif choix == 'voir':
            try:
                with open("mots_de_passe.json", "r") as fichier:
                    donnees = json.load(fichier)
                afficher_mots_de_passe(donnees)
            except (FileNotFoundError, json.JSONDecodeError):
                print("Aucun mot de passe enregistré.")
        elif choix == 'quitter':
            break
        else:
            print("Choix non valide.")

if __name__ == "__main__":
    main()
