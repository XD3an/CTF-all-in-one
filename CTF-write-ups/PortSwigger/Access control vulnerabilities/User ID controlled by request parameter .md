# User ID controlled by request parameter 

## Information
---

- [PortSwigger - Lab: User ID controlled by request parameter ](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter)

This lab has a horizontal privilege escalation vulnerability on the user account page.

To solve the lab, obtain the API key for the user carlos and submit it as the solution.

You can log in to your own account using the following credentials: wiener:peter 

## Solution
---

1. 透過 **wiener:peter** 進行登入。

2. 可以發現 url 後方 **/my-account?id=wiener**是透過 **id** 進行操作，嘗試修改 **id=carlos**。

3. 獲取並提交 carlos API key。