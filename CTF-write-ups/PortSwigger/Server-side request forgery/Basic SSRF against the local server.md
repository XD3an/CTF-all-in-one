# Basic SSRF against the local server

## Information
---

- [PortSwigger - Lab: Basic SSRF against the local server](https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-localhost)

This lab has a stock check feature which fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos. 

## Solution
---

1. 嘗試使用 **check** 鍵查看回傳結果，可以發現回傳為數字。

2. 利用 **Burp Suite** 對 **check** Request 進行攔截，發現是利用staockApi 加上一段 url 。

3. 嘗試更改參數為以下
    ```
    stockApi=http://localhost/admin
    ```
    - 可以發現成功登入。

4. 嘗試點擊 delete 會發現隨然權限不允許，但是可以得到 url 作為下一步的重要資訊。
    ```
    .../admin/delete?username=carlos
    ```
4. 嘗試將參數改為以下以達到題目目標。
    ```
    stockApi=http://localhost/admin/delete?username=carlos
    ```
