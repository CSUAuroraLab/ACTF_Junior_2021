import os
from Crypto.Util.number import *
from binascii import hexlify, unhexlify

banner = '''
               _  ___        _   _           _      ____                      
 _ __ ___   __| |/ _ \      | | | | __ _ ___| |__  / ___| __ _ _ __ ___   ___ 
| '_ ` _ \ / _` | (_) |_____| |_| |/ _` / __| '_ \| |  _ / _` | '_ ` _ \ / _ \\
| | | | | | (_| |\__, |_____|  _  | (_| \__ \ | | | |_| | (_| | | | | | |  __/
|_| |_| |_|\__,_|  /_/      |_| |_|\__,_|___/_| |_|\____|\__,_|_| |_| |_|\___|
'''

def md9(m):
    n, N = 32, 2**256
    h = 69444099843545663157429813687097031070079259699713394209624552060334679683924
    g = 91404868204801963538299172115753433950696139669081509476098772951762196709558
    assert(isinstance(m, bytes) and len(m) == n)
    for x in m:
        h = ((h + x) * g) % N
    return long_to_bytes(h)


def challenge():
    for i in range(5):
        m1 = input("> ")
        m2 = input("> ")
        try:
            m1, m2 = unhexlify(m1), unhexlify(m2)
            if m1 != m2:
                if md9(m1) != md9(m2):
                    print("Failed!")
                    return
                else:
                    print("{} win!".format(i+1))
            else:
                print("Foolish try!")
                return
        except:
            print("Something your input is wrong!")
            return
    flag = os.environ.get('FLAG')
    print("Win!Here is the flag: {}".format(flag))


def main():
    print(banner)
    challenge()


if __name__ == '__main__':
    main()
