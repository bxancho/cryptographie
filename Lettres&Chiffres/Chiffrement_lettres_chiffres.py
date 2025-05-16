# chiffrement.py

def lettre_vers_nombre(lettre):
    """Convertit une lettre majuscule en nombre (A=0, ..., Z=25)."""
    return ord(lettre.upper()) - ord('A')

def nombre_vers_lettre(nombre):
    """Convertit un nombre (0-25) en lettre majuscule."""
    return chr(nombre + ord('A'))

def chiffrer(message):
    """Chiffre un message texte en une suite de nombres, avec conservation des espaces."""
    chiffres = []
    for char in message:
        if char.isalpha():
            chiffres.append(str(lettre_vers_nombre(char)))
        elif char == ' ':
            chiffres.append('_')  # On utilise '/' pour représenter un espace
    return ' '.join(chiffres)

def dechiffrer(message_code):
    """Déchiffre une suite de nombres et '/' en texte, '/' représentant un espace."""
    elements = message_code.split()
    lettres = []
    for element in elements:
        if element == '_':
            lettres.append(' ')
        elif element.isdigit():
            lettres.append(nombre_vers_lettre(int(element)))
    return ''.join(lettres)
