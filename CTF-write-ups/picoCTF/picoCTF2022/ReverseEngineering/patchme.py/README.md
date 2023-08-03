# patchme.py

## Information

### Description
Can you get the flag?
Run this Python program in the same directory as this encrypted flag.

### Hints
(None)

## Solution
將條件判斷改為 not ，也就是使條件不成立即可。
```py
if( not (user_pw == "ak98" + \
                   "-=90" + \
                   "adfjhgj321" + \
                   "sleuth9000")):
        print("Welcome back... your flag, user:")

        decryption = str_xor(flag_enc.decode(), "utilitarian")
        print(decryption)
        return
```
