from aes_cbc import encrypt, decrypt

def main():
    password = input("Mot de passe : ")
    message = input("Message à chiffrer : ")

    salt, iv, ciphertext = encrypt(message, password)
    print(f"\nMessage chiffré : {ciphertext.hex()}")
    print(f"Sel :             {salt.hex()}")
    print(f"IV :              {iv.hex()}")

    # Déchiffrement test
    decrypted = decrypt(salt, iv, ciphertext, password)
    print("")
    print(f"Message déchiffré : {decrypted}")

if __name__ == "__main__":
    main()
