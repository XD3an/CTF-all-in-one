# File path traversal, traversal sequences blocked with absolute path bypass

## Information
---

- [PortSwigger - Lab: File path traversal, traversal sequences blocked with absolute path bypass](https://portswigger.net/web-security/file-path-traversal/lab-absolute-path-bypass)

This lab contains a file path traversal vulnerability in the display of product images.

The application blocks traversal sequences but treats the supplied filename as being relative to a default working directory.

To solve the lab, retrieve the contents of the /etc/passwd file. 

## Solution
---

1. 從獲取圖片的 Responce 中可以看出有個參數 **filename**，猜測是用來獲取檔案的參數。

2. 更改 **filename** 參數，將 **filename** 改成 **/etc/passwd** 的字串形式，使 Respoce 回傳 **/etc/passwd** 的內容。
    ```
    GET /image?filename=/etc/passwd HTTP/1.1
    ...
    ```