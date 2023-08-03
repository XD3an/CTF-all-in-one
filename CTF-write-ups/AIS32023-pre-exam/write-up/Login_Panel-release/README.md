# Login Panel

## Information

- `MyFirstCTF` `Easy`
- `Web`

Login Panel 網站採用了隱形 reCAPTCHA 作為防護機制，以確保只有人類的使用者能夠登入 admin 的帳號。你的任務是找到一個方法來繞過 reCAPTCHA，成功登入 admin 的帳號。

你可以使用各種技術和手段來達成目標，可能需要進行一些網站分析、程式碼解讀或其他形式的攻擊。請注意，你需要遵守道德規範，不得進行任何非法或有害的行為。

當你成功登入 admin 的帳號後，你將能夠獲得 FLAG。請將 FLAG 提交至挑戰平台，以證明你的成功。

Author: Ching367436

## Solution

題目提供 src 跟 config 可以看，透過其中內容推敲即可。
首先一開始進入會看到一個 Login 頁面，明顯是要考驗 SQL Injection 的能力，而且還是個裸體的 SQL Injection。

- Login 頁面存在 SQL Injection 漏洞。
    - Username: `admin`
    - Password: `' OR 1=1--`
- 若失敗會導入至其他頁面...XD

登入後，會發現存在 2fa 雙因子認證頁面，但明顯是我們是得不到其中的 code，實則是要你自行重定向至其他頁面。

- 其中透過給予的 src，可以發現存在一個 `dashboard` 頁面可以使用，當使用 `admin` 權限訪問即可得到 flag。