from idc import *

start = 0x40302F
end = 0x4030CB
enc_flag = []
i = start
while i <= end:
    enc_flag.append(get_operand_value(i, 1))
    i = find_code(i,SEARCH_DOWN)
print(len(enc_flag))
for i in enc_flag:
    print(chr(i^0x61),end = '')
