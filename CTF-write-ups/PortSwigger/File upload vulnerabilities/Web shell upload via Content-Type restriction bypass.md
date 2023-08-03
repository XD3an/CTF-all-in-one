# Web shell upload via Content-Type restriction bypass

## Information
---

- [PortSwigger - Lab: Web shell upload via Content-Type restriction bypass](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-content-type-restriction-bypass)

This lab contains a vulnerable image upload function. It attempts to prevent users from uploading unexpected file types, but relies on checking user-controllable input to verify this.

To solve the lab, upload a basic PHP web shell and use it to exfiltrate the contents of the file /home/carlos/secret. Submit this secret using the button provided in the lab banner.

You can log in to your own account using the following credentials: wiener:peter 

## Solution
---

1. 以 **wiener:peter** 進行登入。

2. 上傳以下腳本。
    ```php
    <?php echo file_get_contents('/home/carlos/secret'); ?>
    ```

3. 利用 **Burp Suite** 攔截 Request。

4. 更改 Content-Type 為 **image/jpeg** 或 **image/png**。

5. 瀏覽 **avatar** 獲取腳本執行結果。

6. 提交答案。