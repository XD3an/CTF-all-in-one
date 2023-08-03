# robot

## Information

- `Misc`

Are you a robot?

Note: This is NOT a reversing or pwn challenge. Don't reverse the binary. It is for local testing only. You will actually get the flag after answering all the questions. You can practice locally by running ./robot AIS3{fake_flag} 127.0.0.1 1234 and it will run the service on localhost:1234.

Author: toxicpie

nc chals1.ais3.org 12348

## Solution

僅須根據輸出的運算式進行運算輸入結果即可，這邊提供兩種解法。

- 手動，如果速度夠快沒問題。

- 自動，腳本。
    - 使用 [正則表達式] 抓 數字與操作。
    ```py
    from pwn import *
    import re

    context.log_level = 'DEBUG'

    def main():
        p = remote(host='chals1.ais3.org', port=12348)

        info(p.recvuntil(b'Timeout is 90 seconds\n'))
        info(p.recvuntil(b"Answer 30 easy math questions to get the flag. Let's go!\n"))

        while True:
            try:
                line = p.recvuntil(b'\n').decode().strip()
                info(line)

                int_list = re.findall(r'\d+', line)
                op_list = re.findall(r'[\+\-\*\/]', line)
                print(int_list, ' ',op_list)

                if '+' in op_list:
                    res = int(int_list[0]) + int(int_list[1])
                elif '-' in op_list:
                    res = int(int_list[0]) - int(int_list[1])
                elif '*' in op_list:
                    res = int(int_list[0]) * int(int_list[1])
                elif '/' in op_list:
                    res = int(int_list[0]) / int(int_list[1])
                else:
                    info(line)
                    print(p.recv())
                    continue
                p.sendline(str(res).encode())

            except:
                pass

    if __name__=='__main__':
        main()

    ```
    