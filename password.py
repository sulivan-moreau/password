import re

def demander_mot_de_passe():
    return input("Choisissez un mot de passe : ")

def verifier_exigences(mot_de_passe):
    # Vérifie si le mot de passe respecte les exigences de sécurité
    return (
        len(mot_de_passe) >= 8 and
        re.search("[A-Z]", mot_de_passe) and
        re.search("[a-z]", mot_de_passe) and
        re.search("[0-9]", mot_de_passe) and
        re.search("[!@#$%^&*]", mot_de_passe)
    )

# Programme principal
if __name__ == "__main__":
    mot_de_passe_valide = False

    while not mot_de_passe_valide:
        mot_de_passe = demander_mot_de_passe()

        if verifier_exigences(mot_de_passe):
            print("Mot de passe valide !")
            mot_de_passe_valide = True
        else:
            print("Le mot de passe ne respecte pas les exigences. Veuillez réessayer.")
