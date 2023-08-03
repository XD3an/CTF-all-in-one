# User ID controlled by request parameter with data leakage in redirect

## Information
---

- [PortSwigger - Lab: User ID controlled by request parameter with data leakage in redirect ](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-data-leakage-in-redirect)

This lab contains an access control vulnerability where sensitive information is leaked in the body of a redirect response.

To solve the lab, obtain the API key for the user carlos and submit it as the solution.

You can log in to your own account using the following credentials: wiener:peter 

## Solution
---

1. 以 **winener:peter** 進行登入。

2. 透過**更改參數 `id`** 來獲取 **carlos** 權限。

3. 利用 **Burp Suite**可以發現過程是透過重定向的方式，最後會回到登入畫面。

4. 透過 **Burp Suite** 抓取重定向過程中的資料，存在 **carlos** 的成功登入畫面(包括 API key)。

5. 提交 API key。