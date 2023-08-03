# vault-door-3

## Information

### Description

This vault uses for-loops and byte arrays. The source code for this vault is here: VaultDoor3.java

### Hints

1. Make a table that contains each value of the loop variables and the corresponding buffer index that it writes to.

## Solution

- Java
    - 觀察原始碼，其中透過一系列操作，最終的結果必須為 `jU5t_a_sna_3lpm18g947_u_4_m9r54f`。
    ```java
        public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18g947_u_4_m9r54f");
    }
    ```

- 利用 python 逆向重建原本的 password(flag)。
    ```py
    not_flag = 'jU5t_a_sna_3lpm18g947_u_4_m9r54f'

    flag = ''.ljust(32, '1')
    flag = list(flag)

    print(flag)

    for i in range(8):
        flag[i] = not_flag[i]

    for i in range(8, 16):
        flag[i] = not_flag[23-i]

    for i in range(16, 32, 2):
        flag[i] = not_flag[46-i]

    for i in range(31, 16, -2):
        flag[i] = not_flag[i]


    print('picoCTF{', ''.join(flag), '}', sep='')
    ```
