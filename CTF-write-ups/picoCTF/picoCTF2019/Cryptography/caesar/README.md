# caesar

## Information

### Description

Decrypt this message.

### Hints

1. caesar cipher tutorial

## Solution

- [caesar](https://en.wikipedia.org/wiki/Caesar_cipher)
    
### Tools

- [decode](https://www.dcode.fr/chiffre-cesar)

- python
    ```py
    class CaserCipher:
    def __init__(self):
        pass
    # Encrypto
    def encrypto_caser(self, plaintext: str, n: int) -> str:
        '''
            C = (P + k) mod 26
        '''
        # Declare a string
        result = str()
        # Encrypt 0 to len(text)
        for i in range(len(plaintext)):
            # temporary storage each char to a
            a = plaintext[i]
            # Encrypt 'A'-'Z' & 'a'-'z'
            if (65 <= ord(a) and ord(a) <= 90) or ( 97 <= ord(a) and ord(a) <= 122):
                if (65 <= ord(a) and ord(a) <= 90):      # uppercase
                    result += chr((ord(a)+n-65)%26+65)
                elif (97 <= ord(a) and ord(a) <= 122):   # lowercase
                    result += chr((ord(a)+n-97)%26+97)
            else:
                result += plaintext[i]
        # return result(cipher text)
        return result


    # decrypto
    def decrypto_caser(self, ciphertext: str, n: int) -> str:
        '''
            p = (C - k) mod 26
        '''
        result = str()
        for i in range(len(ciphertext)):
            a = ciphertext[i]
            if ((65 <= ord(a) and ord(a) <= 90) or (97 <= ord(a) and ord(a) <= 122)):
                if (65 <= ord(a) and ord(a) <= 90):
                    result +=  chr((ord(a)-n-65)%26+65)
                elif (97 <= ord(a) and ord(a) <= 122):
                    result += chr((ord(a)-n-97)%26+27)
            else:
                result += plaintext[i]
        return result

    # brute force attack
    def brute_force(self, ciphertext: str) -> None:
        # Testing 26 times (using all shift possible)
        for n in range(26):
            # Declare a string
            result = str()
            # Decrypto 0 to len(cipher)
            for i in range(len(ciphertext)):
                # temporary storage each char to a
                a = ciphertext[i]
                # Decrypt 'A'-'Z' & 'a'-'z'
                if (65 <= ord(a) and ord(a) <= 90) or ( 97 <= ord(a) and ord(a) <= 122):
                    if (65 <= ord(a) and ord(a) <= 90):      # uppercase
                        result += chr((ord(a)+n-65)%26+65)
                    elif (97 <= ord(a) and ord(a) <= 122):   # lowercase
                        result += chr((ord(a)+n-97)%26+97)
                else:
                    result += ciphertext[i]
            # print result possible
            print(result)

    if __name__=='__main__':
        CaserCipher = CaserCipher()
        
        # open and read ciphertext
        ciphertext = str()
        with open('ciphertext', 'r') as f:
            ciphertext = f.read()

        # brute force
        print("Brute force attack case: ")
        print(f"\"{ciphertext}\" to plain text (Bute-force attack)")
        CaserCipher.brute_force(ciphertext[8:-1])
    ```