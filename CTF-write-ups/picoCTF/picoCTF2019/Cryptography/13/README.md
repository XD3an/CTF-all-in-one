# 13

## Information

### Description

Cryptography can be easy, do you know what ROT13 is? cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}

### Hints

1. This can be solved online if you don't want to do it by hand!

## Solution

- [ROT13](https://en.wikipedia.org/wiki/ROT13)
    

### Tools    
- [cyberchef](https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,13)&input=Y3ZwYlBHU3thYmdfZ2JiX29ucV9ic19uX2NlYm95cnp9Cg)

- python
    ```py
    def rot13(plaintext: str) -> str:
    return ''.join([chr((ord(letter) - 65 + 13) % 26 + 65)
                        if 65 <= ord(letter) <= 90
                        else letter
                    for letter in plaintext.upper()])

    # Executes the main function
    if __name__ == '__main__':
        plaintext = 'cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}'
        print(rot13(plaintext))
    ```