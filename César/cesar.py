
def chiffrer_cesar(message, decalage=4):
    """Chiffre un message en utilisant le code César avec un décalage donné."""
    resultat = ""
    for char in message:
        if char.isalpha():                                                          # Vérifie si c'est une lettre (pour gérer les espaces par la suite)
            base = ord('A') if char.isupper() else ord('a')                         # On sépare majuscule et minuscule dans table ASCII
            lettre_code = chr((ord(char) - base + decalage) % 26 + base)
            """
                char = 'D'
                decalage = 4

                base = ord('A')  # 65
                ord('D') - base = 3
                (3 + 4) % 26 = 7
                chr(7 + 65) = 'H'
            """
            resultat += lettre_code
        else:
            resultat += char  # Garde les espaces et ponctuation
    return resultat

def dechiffrer_cesar_tous(message_code):
    """Teste tous les décalages possibles (0 à 25) pour aider à trouver le bon."""
    essais = []
    for d in range(26):
        texte = ""
        for char in message_code:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                lettre = chr((ord(char) - base - d) % 26 + base)
                texte += lettre
            else:
                texte += char
        essais.append((d, texte))
    return essais
