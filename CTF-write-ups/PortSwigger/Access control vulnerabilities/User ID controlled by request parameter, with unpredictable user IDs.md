# User ID controlled by request parameter, with unpredictable user IDs

## Information
---

- [PortSwigger - Lab: User ID controlled by request parameter, with unpredictable user IDs ](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-unpredictable-user-ids)

This lab has a horizontal privilege escalation vulnerability on the user account page, but identifies users with GUIDs.

To solve the lab, find the GUID for carlos, then submit his API key as the solution.

You can log in to your own account using the following credentials: wiener:peter

## Solution
---

1. 透過 **wiener:peter** 進行登入。

2. 可以發現 url 後方是接 **id** 作為參數使用。

3. 經過查找可以發現每一篇文章下的作者是可以進行點擊的，並可以在 url 中看到與 **id** 很相似的參數 **userid**。

4. 利用 **carlos** 的 **userid** 作為 **id** 使用，登入至 **carlos**的頁面當中。

5. 提交 API key。 
