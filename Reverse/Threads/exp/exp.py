enc = [0xb7,0x8a,0xc8,0x29,0x39,0x78,0x9d,0xd7,0xfa,0x3e,0x40,0x6f,0xa8,0xc8,0xe1,0x37,0x79,0x90,0xbf,0xc0,0x1a,0x24,0x6a,0x8f,0xe1,0xe5,0x0b,0x68,0x69,0xb2,0xde,0xf7,0x24,0x46,0x90,0xb2]

for i in range(len(enc)):
    print(chr((~(enc[i]^((45*i+9)%0x100)))%0x100),end = '')