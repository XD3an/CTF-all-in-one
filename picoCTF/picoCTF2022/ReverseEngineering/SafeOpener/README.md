# Safe Opener

## Information

### Description
Can you open this safe?
I forgot the key to my safe but this program is supposed to help me with retrieving the lost key. Can you help me unlock my safe?
Put the password you recover into the picoCTF flag format like:
picoCTF{password}

### Hints
(None)

## Solution
密碼是通過 base64 加密的，所以我們可以通過 base64解密獲取 flag。

