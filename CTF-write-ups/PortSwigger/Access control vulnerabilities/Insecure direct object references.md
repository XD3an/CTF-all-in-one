# Insecure direct object references

## Information
---

- [PortSwigger - Lab: Insecure direct object references](https://portswigger.net/web-security/access-control/lab-insecure-direct-object-references)

This lab stores user chat logs directly on the server's file system, and retrieves them using static URLs.

Solve the lab by finding the password for the user carlos, and logging into their account. 

## Solution
---

1. 進入 **Live chat** 頁面。

2. 利用 **Burp Suite** 攔截點擊 **View transcript**後的 Request。

3. 通過 Request 可以發現其是利用 **/2.txt** 去獲取內容，嘗試更改數字部分。

4. 改至 **1.txt** 可以看到獲取一段關於 **Password** 的對話，將其擷取下來。

5. 利用這組 **Password** 嘗試登入至 carlos。