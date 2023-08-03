# OS command injection, simple case

## Information
---

- [PortSwigger - Lab: OS command injection, simple case](https://portswigger.net/web-security/os-command-injection/lab-simple)



This lab contains an OS command injection vulnerability in the product stock 
checker.

The application executes a shell command containing user-supplied product and store IDs, and returns the raw output from the command in its response.

To solve the lab, execute the whoami command to determine the name of the current user. 

## Solution
---

1. 使用 Burp Suite 攔截 Request。

2. 將 Request 中的參數後方加上 `;whoami`，使 Responce 可以回傳 `whoami` 的結果。
    ```
    productId=6&storeId=1;whoami
    ```