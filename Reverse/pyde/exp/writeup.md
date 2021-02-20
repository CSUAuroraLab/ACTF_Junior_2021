python EXE文件反编译



先将exe文件反编译

```cmd
python pyinstxtractor.py main.exe
```

然后使用winhex添加pyc头部

再将pyc文件反编译成py

```cmd
uncompyle6 -o main.py main.pyc
```

得到源代码

```python
# uncompyle6 version 3.7.2
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: main.py
# Compiled at: 1995-09-28 00:18:56
# Size of source mod 2**32: 272 bytes
from Crypto.Cipher import AES
import base64

def add_16(par):
    if type(par) == str:
        par = par.encode()
    while len(par) % 16 != 0:
        par += b'\x00'

    return par


flag = input()
result = (lambda data, key, iv: str((base64.b64encode(AES.new(add_16(key), AES.MODE_CBC, add_16(iv)).encrypt(lambda s: s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)(data).encode('utf-8')))), encoding='utf-8'))(flag, 'Are_you_Ok?hahah', '0102030405060708')
en_flag = 'NZRk3DxfmxGHwiQkDJQlqrTvUb2icaiUSIdnFn+WMb0='
if en_flag == result:
    print('Success')
else:
    print('No')
```



使用[CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)AES_Decrypt(%7B'option':'UTF8','string':'Are_you_Ok?hahah'%7D,%7B'option':'UTF8','string':'0102030405060708'%7D,'CBC','Raw','Raw',%7B'option':'Hex','string':''%7D)&input=TlpSazNEeGZteEdId2lRa0RKUWxxclR2VWIyaWNhaVVTSWRuRm4rV01iMD0)得到flag

# flag

```flag
actf{Thi5_7s_A3S_CBC}
```

