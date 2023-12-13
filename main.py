import string
import hashlib

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

# Programme
nom_utilisateur = input("Entrez votre nom d'utilisateur : ")
mdp_saisi = mdp_user()
print("Votre mot de passe est valide")
hashed_password = hashed_mdp(mdp_saisi)
mdp_hache = hashed_mdp(mdp_saisi)
print("Voici le mot de passe haché :", mdp_hache)
