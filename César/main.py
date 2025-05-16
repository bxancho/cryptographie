from cesar import chiffrer_cesar, dechiffrer_cesar_tous

def menu():
    print("=== Code César ===")
    print("1. Chiffrer une phrase (décalage de 4)")
    print("2. Déchiffrer un message")
    print("3. Quitter")

while True:
    menu()
    choix = input("Choisissez une option (1/2/3) : ")

    if choix == "1":
        texte = input("Entrez le message à chiffrer : ")
        code = chiffrer_cesar(texte, decalage=4)
        print("Message chiffré :", code)

    elif choix == "2":
        texte = input("Entrez le message codé à déchiffrer : ")
        essais = dechiffrer_cesar_tous(texte)
        print("\nTentatives pour chaque décalage :")
        print("")
        for decalage, tentative in essais:
            print(f"Décalage {decalage} : {tentative}")

    elif choix == "3":
        print(" A+ ")
        break

    else:
        print("Option invalide. Veuillez entrer 1, 2 ou 3.")
