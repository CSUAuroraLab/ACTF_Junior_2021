from Crypto.Util.number import *
from flag import A,B,seed,flag

S=[seed]

def rand(mod):
    S.append((S[-1]*A+B)%mod)
    return S[-1]

def fill(Str:str):
    Len = len(Str)
    res = 43 - Len
    return '0'*res+Str

def encrypto(x:str,s:str):
    x=int(x)
    s=int(s)
    c=(x+s)%2
    return str(c)

m = flag
m = bytes_to_long(m)
m=str(bin(m))[2:]
c = ""
for i in range(5):
    s=rand(233333333333)
    s=str(bin(s))[2:]
    s=fill(s)
    for j in range(43):
        newc=encrypto(m[i*43+j],s[j])
        c=c+newc
print(c)


