import re, sys, hashlib
from binascii import hexlify, unhexlify
from pwn import *

io = remote(sys.argv[1], sys.argv[2])
# context.log_level = 'debug'

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def sign_up():
    username = "0xDktb"
    io.sendlineafter("> ", username)
    msg = io.recvline().strip().decode()
    token = unhexlify(re.findall(r"token=(.*)", msg)[0])
    return token

def separator_oracle(token):
    token = hexlify(token)
    io.sendlineafter("> ", token)
    msg = io.recvline().strip().decode()
    if 'Welcome' in msg:
        return True
    else:
        return False

def crack_key(token):
    username = "0xDktb"
    username = hashlib.sha256(username.encode("latin-1")).hexdigest()[26:38]
    salt = ''
    xor_list = [ord(_) ^ ord('|') for _ in '0123456789abcdef']
    for i in range(len(username) + 1, len(username) + 17):
        for j in range(len(xor_list)):
            if not separator_oracle(token[:i] + bytes([token[i] ^ xor_list[j]]) + token[i+1:]):
                salt += hex(j)[2:]
                break
        print(salt)
    token_pt = username + '|' + salt + '|0'
    key = xor(token_pt.encode(), token)
    return key, salt

def get_flag(key, salt):
    payload = "{}|{}|{}".format(hashlib.sha256(b"cxlover_yyds").hexdigest()[26:38], salt, 1)
    token = hexlify(xor(payload.encode(), key))
    io.sendlineafter("> ", token)
    # io.sendlineafter("> ", salt)
    io.interactive()

def main():
    token = sign_up()
    key, salt = crack_key(token)
    get_flag(key, salt)

if __name__ == '__main__':
    main()
