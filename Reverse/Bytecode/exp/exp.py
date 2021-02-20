import hashlib
import itertools

enc2 = [33, 64, 37, 29, 45, 24, 47, 29, 43, 25, 44, 28, 125, 31, 44, 78, 122, 79, 120, 72, 122, 24, 46, 31, 121, 24,
        122, 31, 123, 74, 115, 22, 38, 20, 38, 69, 118, 68, 125, 79, 124]
enc1 = [65, 66, 126, 106, 124, 95, 89, 85, 98, 60, 105, 80, 66, 88, 126, 63, 100, 63, 68, 68, 85]
key = [0x20, 0x21, 0x0a, 0x0c, 0x07, 0x0f]
part1 = [chr(m ^ k) for m, k in zip(enc1, itertools.cycle(key))]
print(''.join(part1))
encrypted_flag = []
for i in range(len(enc2) - 1, -1, -1):
    t = enc2[i] ^ enc2[i - 1]
    encrypted_flag.insert(0, chr(int(t)))
encrypted_flag = ''.join(encrypted_flag[1:])
print(encrypted_flag)
flag = 'actf{Pyth0n_byt3c0de_'
for i in range(100000, 999999):  # i是我们要输入的六位数字，显然范围是100000~999999
    s = flag + str(i) + '}'
    x = hashlib.sha1(s.encode())
    if x.hexdigest() == encrypted_flag:
        print(s)
        break
