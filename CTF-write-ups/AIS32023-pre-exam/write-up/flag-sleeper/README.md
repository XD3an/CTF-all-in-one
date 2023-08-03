# Flag Sleeper

## Information

- `Hello World 🌱` `Easy` `MyFirstCTF`
- `Reverse`

Taking a nap before entering the world of AIS3 is important! A good hacker requires good sleep, and so does this flag checker.

Author: TwinkleStar03 ✨

## Solution
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

透過內容可以看出其結果會是 argv[1] 與前方已經定義的 v8, v9, v10 進行操作比對。
    - 操作如下
        ```c
        v6 = rand() % 52;
        v7 = v8[v6];
        if ( a2[1][v7] != (v10[v6] ^ v9[v6]) )
            ...
        ```

- 綜上所知，可以得到以下內容。
    - v8 被當作 index。
    - v9, v10 是操作比對的目標對象。
    - 操作為 a2[1][v8[i]] = v9[i]^v10[i]，其中 i 為 rand()%52。
    - rand() 沒甚麼用處。

- python 腳本
    - 整理 v8, v9, v10，根據邏輯逆推。
    ```py
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