# Blind OS command injection with time delays

## Information
---

- [PortSwigger - Lab: Blind OS command injection with time delays](https://portswigger.net/web-security/os-command-injection/lab-blind-time-delays)

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response.

To solve the lab, exploit the blind OS command injection vulnerability to cause a 10 second delay. 

## Solution
---

1. 透過以下 payload 對每一個參數做檢查，只要超過 10 秒回應 Responce 就大機率代表出現 command injection 漏洞。
    ```
    ;ping+-c+10+127.0.0.1;
    ```

2. 可以發現 email 這一欄參數明顯回應過慢。