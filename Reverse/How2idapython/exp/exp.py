from idc import *

enc_flag = [0xb8,0xa3,0x64,0xb8,0xbd,0xb4,0x98,0xf3,0x7d,0x8c,0xa8,0xa6,0x65,0xa7,0xf0,0x3c,0x9d,0x8d,0xcf,0x1b,0x63,0x8,0x7b,0xe7,0x7e,0xf2,0x8f,0x98,0xba,0xd6,0x53,0xdb,0x17,0xd4,0xf9,0xfb,0x93,0x95,0x3c,0x1f,0x7c,0xfb,0x89,0x31,0x9a,0xb2,0x8]
start_addr = 0x40162a
end_addr = 0x40354b
i = start_addr

while(i<=end_addr):
    code = GetDisasm(i)
    index = None
    calc = None
    if '[rdx]' in code:
        index = 0
    else:
        index = get_operand_value(i, 1)
    i = find_code(i,SEARCH_DOWN)
    calc = get_operand_value(i, 1)
    #print("calc:",calc,",index:",index)
    enc_flag[index] = (enc_flag[index] - calc) & 0xff
    i = find_code(i,SEARCH_DOWN)
    i = find_code(i,SEARCH_DOWN)

for i in enc_flag:
    print(chr(i),end = '')