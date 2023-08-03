# vault-door-5

## Information

### Description

In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! The source code for this vault is here: VaultDoor5.java

### Hints

1. You may find an encoder/decoder tool helpful, such as https://encoding.tools/

2. Read the wikipedia articles on URL encoding and base 64 encoding to understand how they work and what the results look like.

## Solution

- Password(flag) 是先被 URL encode 再 base64 encode 後再進行判斷，所以只要根據順序逆向。
    ```py
    import base64

    str = 'JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTY1JTMzJTMxJTM1JTMyJTYyJTY2JTM0'
    url_encode = base64.b64decode(str).decode().split("%")
    print(url_encode)

    flag='picoCTF{'
    for i in url_encode:
        if i == '':
            continue
        flag += chr(int(i, 16))
    flag+='}'

    print(flag)

    ```