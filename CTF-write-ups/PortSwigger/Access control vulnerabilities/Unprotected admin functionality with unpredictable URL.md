# Unprotected admin functionality with unpredictable URL

## Information
---

- [PortSwigger - Lab: Unprotected admin functionality with unpredictable URL](https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality-with-unpredictable-url)

This lab has an unprotected admin panel. It's located at an unpredictable location, but the location is disclosed somewhere in the application.

Solve the lab by accessing the admin panel, and using it to delete the user carlos. 

## Solution
---

1. 找出 **admin** 的權限獲取頁面 (**/admin-xxxxxx**)。
    1. **Burp Suite**: **Target**-> **Site-map**，觀察頁面。
    2. **F12**: 從 HTML 中找出相關資訊。

2. 嘗試頁面 **/admin-xxxxxx**。