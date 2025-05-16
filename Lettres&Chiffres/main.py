# main.py

from Chiffrement_lettres_chiffres import chiffrer, dechiffrer

def menu():
    print("===Système de chiffrement===")
    print("1. Chiffrer un message")
    print("2. Déchiffrer un message")
    print("3. Quitter")

while True:
    menu()
    choix = input("Choisissez une option (1/2/3) : ")

    if choix == "1":
        texte = input("Entrez le message à chiffrer : ")
        code = chiffrer(texte)
        print("Message chiffré :", code)

    elif choix == "2":
        code = input("Entrez le message à déchiffrer : ")
        texte = dechiffrer(code)
        print("Message déchiffré :", texte)

    elif choix == "3":
        print(" A+ ")
        break

    else:
        print("Option invalide. Veuillez entrer 1, 2 ou 3.")
