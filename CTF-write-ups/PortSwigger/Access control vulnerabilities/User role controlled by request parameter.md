# User role controlled by request parameter

## Information
---

- [PortSwigger - Lab: User role controlled by request parameter](https://portswigger.net/web-security/access-control/lab-user-role-controlled-by-request-parameter)

This lab has an admin panel at /admin, which identifies administrators using a forgeable cookie.

Solve the lab by accessing the admin panel and using it to delete the user carlos.

You can log in to your own account using the following credentials: wiener:peter 

## Solution
---

1. 更改 cookies 中 Admin 的值為 **True**。

2. 刪除 calors。