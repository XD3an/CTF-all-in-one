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
