# Simply Reverse

## Information

- `MyFirstCTF` `Baby`
- `Reverse`

Just reverse it!

## Solution
題目提供一個壓縮檔，其中內容只包含一個 ELF 格式 64bits 的 binary 檔，透過 IDA Pro 或 Ghidra 等工具反組譯、反編譯一下。

觀察其中內容，可以發現存在一個 `verify(_int64 a1)` 的 function，之後程式的運行將因為騎回傳的結果繼續，若為 True 則正確並輸出 "Correct key!"，反之則失敗並輸出 "Wrong key!"。

觀察 `verify(_int64 a1)` 內容。

- IDA Pro 一下
    ```c
    _BOOL8 __fastcall verify(__int64 a1)
    {
    int i; // [rsp+14h] [rbp-4h]

    for ( i = 0; *(_BYTE *)(i + a1); ++i )
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

    ```py
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
