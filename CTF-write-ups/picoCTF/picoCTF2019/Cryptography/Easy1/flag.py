def veginere(plaintext: str, key: str) -> str:
    ciphertext = str()
    # plain text process
    plaintext = plaintext.upper()
    plaintext = plaintext.replace(" ", "")
    # key process
    key = key.replace(" ","")
    # encryption
    for i in range(len(plaintext)):
        if (plaintext[i].isalpha()):
            ciphertext += chr((ord(plaintext[i])+ord(key[i%len(key)]))%26 + 65)
        else:
            continue
    return ciphertext

def de_veginere(ciphertext: str, key: str) -> str:
    plaintext = str()
    #cipher text process
    ciphertext = ciphertext.upper()
    ciphertext = ciphertext.replace(" ", "")
    # key process
    key = key.replace(" ", "")
    # decryption
    key_index = 0
    for i in range(len(ciphertext)):
        if (ciphertext[i].isalpha()):
            shift = ord(key[key_index]) - ord('A')    # shift = ord(key) - ord('A')
            plaintext += chr((ord(ciphertext[i])-shift-65)%26+65)
        else:
            plaintext += ciphertext[i]
        key_index = (key_index+1)%len(key)
    return plaintext    

if __name__=="__main__":
    ciphertext, key = 'UFJKXQZQUNB', 'SOLVECRYPTO'
    flag = de_veginere(ciphertext, key)
    print(f'picoCTF{{{flag}}}')