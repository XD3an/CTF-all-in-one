# miniRSA

## Information

### Description

Let's decrypt this: ciphertext? Something seems a bit small.

### Hints

1. RSA tutorial

2. How could having too small an e affect the security of this 2048 bit key?

3. Make sure you don't lose precision, the numbers are pretty big (besides the e value)

## Solution

### RSA

- RSA step
    1. 隨意選擇兩個大質數 $p$ 與 $q(p \not = q)$，計算 $N (N=pq)$。
    2. 求 $r = \phi(N) = \phi(p) \times \phi(q) = (p-1)(q-1)$。
    3. 選擇一個小於 $r$ 的整數 $e$，使 $e$ 與 $r$ 互質 ( $\text{GCD}(e, \phi(N)) = 1$ )。
    4. 求 $e$ 關於 $r$ 的模反元素 $d (ed\equiv1\mod{r})$。

- Encryption
    - $ciphertext = plaintext^e \mod{N}$

- Decryption
    - $plaintext = ciphertext^d \mod{N}$

### Solve ($e$ too small)

- 因為 **$e$ 太小**，所以可以透過取次方根的方式獲取 $plaintext$，如題 $e=3$ 所以只要取 $ciphertext$ 的立方根即可獲取 $plaintext$。

- python
    ```py
    import gmpy2

    N = 29331922499794985782735976045591164936683059380558950386560160105740343201513369939006307531165922708949619162698623675349030430859547825708994708321803705309459438099340427770580064400911431856656901982789948285309956111848686906152664473350940486507451771223435835260168971210087470894448460745593956840586530527915802541450092946574694809584880896601317519794442862977471129319781313161842056501715040555964011899589002863730868679527184420789010551475067862907739054966183120621407246398518098981106431219207697870293412176440482900183550467375190239898455201170831410460483829448603477361305838743852756938687673
    e = 3
    ciphertext = 2205316413931134031074603746928247799030155221252519872649649212867614751848436763801274360463406171277838056821437115883619169702963504606017565783537203207707757768473109845162808575425972525116337319108047893250549462147185741761825125

    # 計算 ciphertext 的立方根
    plaintext, exact = gmpy2.iroot(ciphertext, 3)

    # 若存在(exact!=False)，則轉成 bytes 類型輸出
    if not exact:
        print("No exact cube root found")
    else:
        print(f"Plaintext: {bytes.fromhex(hex(plaintext)[2:])}")
    ```