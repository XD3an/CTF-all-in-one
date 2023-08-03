# Unprotected admin functionality

## Information
---

- [PortSwigger - Lab: Unprotected admin functionality](https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality)

This lab has an unprotected admin panel.

Solve the lab by deleting the user carlos. 

## Solution
---

1. 嘗試觀察 **/robots.txt** 後發現存在此頁面。
    ```
    User-agent: *
    Disallow: /administrator-panel
    ```
    - 可以從 **/robots.txt** 中發現 **/administrator-pane**

2. 嘗試 **adminstrator-panel**，可以發現成功獲取 **admin** 權限。

3. 刪除 carlos。