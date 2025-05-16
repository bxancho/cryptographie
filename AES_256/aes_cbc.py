from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

BLOCK_SIZE = 16  # AES block size

def pad(data: bytes) -> bytes:
    pad_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([pad_len] * pad_len)

def unpad(data: bytes) -> bytes:
    pad_len = data[-1]
    return data[:-pad_len]

def derive_key(password: str, salt: bytes) -> bytes:
    return PBKDF2(password, salt, dkLen=32, count=100_000)

def encrypt(message: str, password: str) -> tuple[bytes, bytes, bytes]:
    salt = get_random_bytes(16)
    iv = get_random_bytes(16)
    key = derive_key(password, salt)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(message.encode()))

    return salt, iv, ciphertext

def decrypt(salt: bytes, iv: bytes, ciphertext: bytes, password: str) -> str:
    key = derive_key(password, salt)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(ciphertext)
    return unpad(decrypted_padded).decode()
