# User ID controlled by request parameter with password disclosure

## Information
---

- [PortSwigger - Lab: User ID controlled by request parameter with password disclosure](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-password-disclosure)

This lab has user account page that contains the current user's existing password, prefilled in a masked input.

To solve the lab, retrieve the administrator's password, then use it to delete carlos.

You can log in to your own account using the following credentials: wiener:peter 

## Solution
---

1. 以 **wiener:peter** 進行登入。


2. 透過至 My account 頁面更改 **id=administrator** 登入至 **administrator**，並透過 HTML 獲取 **administrator** 的 Password。

3. 利用獲取的 Password 登入至 **administrator**。

4. 刪除 carlos。