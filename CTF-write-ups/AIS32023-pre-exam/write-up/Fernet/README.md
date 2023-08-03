# Fernet

## Information

- `MyFirstCTF` `Baby`
- `Crypto`

你所在的公司最近發生了一起駭客入侵事件，管理員發現駭客使用 Fernet 密碼學來加密了他們的敏感數據。你需要解開被加密的檔案，否則事情就大條了！

## Solution
題目當中提供了 **chal.py**、**output.txt** 兩個檔案，透過觀察可以合理推斷 **output.txt** 是透過 **chal.py** 進行加密，所以要得到原文 (plain text)，必須先了解如何解密。
- [Fernet](): 是一種對稱式加密演算法，使用 AES 和 [HMAC](https://zh.wikipedia.org/zh-tw/HMAC) 摘要算法來實現對稱加密 。
    1. 使用 key 生成 AES、HMAC。
    2. 將 plaintext 作為參數傳遞給 AES，使用 CBC 模式進行加密。
    3. 將 AES 加密後的 key 和 隨機生成的初始化向量（IV）拼接在一起，形成 ciphertext。
    4. 將 ciphertext 作為參數傳給 HMAC ，計算出 ciphertext 的 HMAC 值。
    5. 將 HMAC 值和 ciphertext 進行拼接，形成最終的 ciphertext。

### Encrypt    
加密過程為以下
- Encrypt
    ```py
        def encrypt(plaintext, password):
            salt = os.urandom(16)  
            key = PBKDF2(password.encode(), salt, 32, count=1000, hmac_hash_module=SHA256)  
            f = Fernet(base64.urlsafe_b64encode(key))  
            ciphertext = f.encrypt(plaintext.encode())  
            return base64.b64encode(salt + ciphertext).decode()

        # Usage:
        leak_password = 'mysecretpassword'
        plaintext = FLAG

        # Encrypt
        ciphertext = encrypt(plaintext, leak_password)
        print("Encrypted data:",ciphertext)
    ```
- Step
    1. salt: 使用 `os.urandom(16)` 產生一個長度為 16 Bytes 的隨機值，作為 `salt`。
        ```py
        salt = os.urandom(16)
        ```
    2. key: 使用 `PBKDF2 ` 產生 key，根據一個 salt 、password 生成一個固定長度的 key，其中 `hmac_hash_module` 是指使用 `HMAC`=SHA256。
        ```py
        key = PBKDF2(password.encode(), salt, size=32, count=1000, hmac_hash_module=SHA256)
        ```
    3.  使用 [base64.urlsafe_b64encode(key)](https://docs.python.org/3/library/base64.html#base64.urlsafe_b64encode) 函數將 key 轉換("+"->"-"、"/"->"_"、"=="->"=")，並用 `Fernet`進行初始化。
        ```py
        f = Fernet(base64.urlsafe_b64encode(key))
        ```
    4. 使用 `f.encrypt()` 將 plaintext 進行加密。
        ```py
        ciphertext = f.encrypt(plaintext.encode())
        ```
    5. 最後回傳 ciphertext。

- output.txt
    ```
    Encrypted data: iAkZMT9sfXIjD3yIpw0ldGdBQUFBQUJrVzAwb0pUTUdFbzJYeU0tTGQ4OUUzQXZhaU9HMmlOaC1PcnFqRUIzX0xtZXg0MTh1TXFNYjBLXzVBOVA3a0FaenZqOU1sNGhBcHR3Z21RTTdmN1dQUkcxZ1JaOGZLQ0E0WmVMSjZQTXN3Z252VWRtdXlaVW1fZ0pzV0xsaUM5VjR1ZHdj
    ```

### Decrypt

- 發現其中有可以使用的資訊。
    ```
    leak_password = 'mysecretpassword'
    plaintext = FLAG // not real flag
    ```

- 逆推回去進行解密操作。

- Step
    1. 對 ciphertext 進行 b64decode()，分為 `salt` 與 `ciphertext`。
        - 在 [encrypt](https://cryptography.io/en/latest/fernet/#cryptography.fernet.Fernet.encrypt) 函數中，將 salt 和 ciphertext 進行了拼接，並將其 base64 加密。
    2. 透過 `PBKDF2` 生成原先加密的 key。
        - 因為已經得知 password、salt，所以可以得到加密時使用的 key 。
    3. 透過 `base64.urlsafe_b64encode(key)` 將 key 轉為 base64，並用 `Fernet`進行初始化。
        - 因為已經的到 key，所以可以得到原先加密時所使用的 `Fernet`。
    4. 使用 `f.decrypt()` 進行解密。
```py
def decrypt(ciphertext, password):
    ciphertext = base64.b64decode(ciphertext.encode())
    salt, ciphertext = ciphertext[:16], ciphertext[16:]
    key = PBKDF2(password.encode(), salt, 32, count=1000, hmac_hash_module=SHA256)
    f = Fernet(base64.urlsafe_b64encode(key))
    plaintext = f.decrypt(ciphertext).decode()
    return plaintext
```

## Further Reading

- https://zhuanlan.zhihu.com/p/25278582