# ReadMyCert

## Infromation

### Description

How about we take you on an adventure on exploring certificate signing requests
Take a look at this CSR file here.

### Hints

1. Download the certificate signing request and try to read it.

## Solution

- openssl
    ````sh
    openssl req -in readmycert.csr -noout -text
    ```
    - `openssl`: 使用 openssl。
    - `req`: 用於 certificate request and singing。
    - `in` : 輸入檔案。
    - `noout`: 跳過實際憑證的輸入，僅輸出 CSR 內容。
    - `text`: 使用 text 格式表示。