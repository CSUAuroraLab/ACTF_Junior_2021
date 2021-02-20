from Crypto.Cipher import AES
import base64

def add_16(par):
    if type(par) == str:
        par = par.encode()
    while len(par) % 16 != 0:
        par += b'\x00'
    return par

flag = input()
result = (lambda data,key,iv:str(base64.b64encode(AES.new(add_16(key), AES.MODE_CBC, add_16(iv)).encrypt((lambda s: s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size))(data).encode("utf-8"))),encoding="utf-8"))(flag, "Are_you_Ok?hahah", "0102030405060708")
en_flag = "NZRk3DxfmxGHwiQkDJQlqrTvUb2icaiUSIdnFn+WMb0="
if en_flag == result:
    print("Success")
else:
    print("No")