import hashlib
import itertools
part1 = "actf{Pyth0n_byt3c0de_"
part2 = "114514}"
key = [0x20, 0x21, 0x0a, 0x0c, 0x07, 0x0f]
tmp = input("Part2 of flag:")
if (len(tmp) > 7):
    print("Part2 no more than 7 characters!")
    exit(0)
input1 = []
for i in tmp[0:6]:
    t = str(int(i, 10))
    input1.append(t)
input2 = input("Part1 of flag:")
temp = input2 + ''.join(input1) + '}'
flag = part1 + part2
hash1 = hashlib.sha1(flag.encode('utf-8'))#ae805726250ab3b45702b61fabed19e022c32923
hash2 = hashlib.sha1(temp.encode('utf-8'))
if hash1.hexdigest() == hash2.hexdigest():
    print("You are right!")
else:
    print("Try again!")
    exit(0)
hash1 = hash1.hexdigest().encode()
enc2 = [0x21]
for i in range(0, len(hash1)):
    enc2.append(hash1[i] ^ enc2[i])
print("enc2:",enc2)
enc1 = [ord(m) ^ k for m, k in zip(part1, itertools.cycle(key))]
print("enc1:",enc1)