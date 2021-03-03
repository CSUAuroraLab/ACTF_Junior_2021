# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 21:10:33 2021

@author: mxy
"""
from pwn import *
import time
context.log_level="debug"
p=remote('139.155.83.108',10000)
def bh(number,key):
    ans=number%(key+1)
    print('key+1= ',key+1)
    return ans
p.recvuntil('and the maximum number is ')
key=int(p.recvuntil('\n')[:2])
print('The_key: ',key)
p.sendafter('(y/n)','y\n')

for i in range(6):
    p.recvuntil('There are ')
    number=int(p.recvuntil('stones in the pile at present')[:2])
    player=0
    print('The_number :',number)
    if number%(key+1)!=0:
        payload='n\n'
        player=bh(number,key)
        p.sendafter('Are you sure you want to abandon?(y/n)',payload)
        
    else:
        payload='y\n'
        p.sendafter('Are you sure you want to abandon?(y/n)',payload)
    while True:
        
        p.recvuntil('The current number of pebbles : ')
        number=int(p.recvuntil('\n')[:2])
        player=bh(number,key)
        p.sendafter('You choose number : ',str(player)+'\n')
        time.sleep(0.4)
        if number<=key:
            break
p.interactive()
