def rot13(plaintext: str) -> str:
    return ''.join([chr((ord(letter) - 65 + 13) % 26 + 65)
                        if 65 <= ord(letter) <= 90
                        else letter
                    for letter in plaintext.upper()])

# Executes the main function
if __name__ == '__main__':
    plaintext = 'cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}'
    print(rot13(plaintext))