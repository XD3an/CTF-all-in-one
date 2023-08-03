import base64
from cryptography.fernet import Fernet
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import PBKDF2

def decrypt(ciphertext, password):
    ciphertext = base64.b64decode(ciphertext.encode())
    salt, ciphertext = ciphertext[:16], ciphertext[16:]
    key = PBKDF2(password.encode(), salt, 32, count=1000, hmac_hash_module=SHA256)
    f = Fernet(base64.urlsafe_b64encode(key))
    plaintext = f.decrypt(ciphertext).decode()
    return plaintext

def main():
    leak_password = 'mysecretpassword'
    ciphertext = 'iAkZMT9sfXIjD3yIpw0ldGdBQUFBQUJrVzAwb0pUTUdFbzJYeU0tTGQ4OUUzQXZhaU9HMmlOaC1PcnFqRUIzX0xtZXg0MTh1TXFNYjBLXzVBOVA3a0FaenZqOU1sNGhBcHR3Z21RTTdmN1dQUkcxZ1JaOGZLQ0E0WmVMSjZQTXN3Z252VWRtdXlaVW1fZ0pzV0xsaUM5VjR1ZHdj'

    plaintext = decrypt(ciphertext, leak_password)
    print(plaintext)

if __name__=='__main__':
    main()