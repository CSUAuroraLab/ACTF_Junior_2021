from Crypto.Util.number import *
import gmpy2

def fill(Str:str):
    Len = len(Str)
    res = 43 - Len
    return '0'*res+Str

def decrypto(x:str,s:str):
    x=int(x)
    s=int(s)
    c=(x+s)%2
    return str(c)

_plain = "110000101100011011101000110011001111011011101110110010100110001011000110110111101101101011001010101111101101100011010010111010001"
cipher = "11000010110001110100101111101001101011011110111001100101000011010110011011100101001011101100110011101001010100111010001111000110111010000111110000001111110010010010110000000100101101111011101111111000010010010100000"
mod = 233333333333
len_p = len(_plain)
_cipher = cipher[:len_p]
_s = ""
for i in range(len_p):
    _x = int(_plain[i])
    _y = int(_cipher[i])
    _s = _s + str((_x + _y)%2)

s=[]
for i in range(3):
    s.append(_s[i*43:(i+1)*43])

for i in range(len(s)):
    s[i] = int(s[i],2)

inv = gmpy2.invert(s[0]-s[1],mod)
A = ((s[1]-s[2])*inv)%mod
B = (s[1]-s[0]*(s[1]-s[2])*inv)%mod
for i in range(2):
    s.append((s[-1]*A+B)%mod)

S = ""
for i in s:
    S += fill(bin(i)[2:])

plain = ""
for i in range(len(cipher)):
    plain += decrypto(cipher[i],S[i])

plain = int(plain,2)
print(long_to_bytes(plain))

