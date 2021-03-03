from Crypto.Util.number import *
from binascii import hexlify
from sys import argv
from pwn import *

#context.log_level = 'debug'
io = remote(argv[1], argv[2])

def md9(m):
    n, N = 32, 2**256
    h = 69444099843545663157429813687097031070079259699713394209624552060334679683924
    g = 91404868204801963538299172115753433950696139669081509476098772951762196709558
    assert(isinstance(m, bytes) and len(m) == n)
    for x in m:
        h = ((h + x) * g) % N
    return long_to_bytes(h)

g = 91404868204801963538299172115753433950696139669081509476098772951762196709558
n = 32
N = 2**256

A_list = [[N] + [0] * n]
for i in range(1, n + 1):
    A_list.append([int(pow(g, i - 1, N))] + [int(i == j) for j in range(1, n + 1)])
# Find hash crash(use LLL/BKZ)
A = Matrix(ZZ, A_list)
AL = A.BKZ(block_size=24)
for line in AL:
    if line[0] == 0:
        delta = list(line[1:][::-1])
        break

for j in range(5):
    x1, x2 = [], []
    for i in range(n):
        if delta[i] < 0:
            x1.append(-delta[i] + j)
            x2.append(j)
        else:
            x1.append(j)
            x2.append(delta[i] + j)
    x1 = bytes(x1)
    x2 = bytes(x2)
    if md9(x1) == md9(x2):
        print("[+] {} hash crash has been found".format(j+1))
    io.sendlineafter("> ", hexlify(x1))
    io.sendlineafter("> ", hexlify(x2))
io.interactive()
#io.close()
