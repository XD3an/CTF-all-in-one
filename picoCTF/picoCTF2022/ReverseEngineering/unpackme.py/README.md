# unpackme.py

## Information

### Description
Can you get the flag?
Reverse engineer this Python program.

### Hints
(None)

## Solution

* base64(key_str.encode())
```py
>>> base64.b64encode(key_str.encode())
b'Y29ycmVjdHN0YXBsZWNvcnJlY3RzdGFwbGVjb3JyZWM='
```

* Fernet: 是一種實現高級加密標準（AES）的密碼庫，用於實現对稱加密。它使用128位密鑰和SHA256雜湊算法來保證數據安全性。
```py
>>> Fernet(key_base64)
<cryptography.fernet.Fernet object at 0x7f643e6882b0>
>>> f = Fernet(key_base64)
>>> f.decrypt(payload)
b"\npw = input('What\\'s the password? ')\n\nif pw == 'batteryhorse':\n  print('picoCTF{175_chr157m45_85f5d0ac}')\nelse:\n  print('That password is incorrect.')\n\n"
```

* exec(): 用於執行參數當中所傳入的字串，將其作為 python 程式碼來執行。
```py
>>> exec(plain.decode())
```