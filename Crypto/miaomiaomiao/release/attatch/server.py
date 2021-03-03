import os, time, string, hashlib
from Crypto.Cipher import AES
from Crypto.Util import Counter
from binascii import hexlify, unhexlify
from secret import flag

banner = '''
            |                                       |
  __|\ \  / |  _ \\\\ \   / _ \  __|  |   | |   |  _` |  __|
 (    `  <  | (   |\ \ /  __/ |     |   | |   | (   |\__ \\
\___| _/\_\_|\___/  \_/ \___|_|    \__, |\__, |\__,_|____/
                             _____|____/ ____/
'''

class cxlover_club:
    def __init__(self):
        print(banner)
        self.key = os.urandom(16)
        self.salt = hashlib.sha256(os.urandom(16)).hexdigest()[24:40]
        self.owner = hashlib.sha256(b"cxlover_yyds").hexdigest()[26:38]

    def __check_username(self, username):
        if len(username) == 0 or len(username) > 20 or username == "cxlover_yyds":
            return False
        else:
            return True

    def sign_up(self):
        print("[+] sign up first.")
        self.r = time.localtime(time.time())[5]
        aes = AES.new(self.key, AES.MODE_CTR, counter=Counter.new(128, initial_value=self.r))
        username = input("> ")
        if not self.__check_username(username):
            print("[!] Invalid username!")
            exit(0)
        username = hashlib.sha256(username.encode("latin-1")).hexdigest()[26:38]
        token = hexlify(aes.encrypt("{}|{}|{}".format(username, self.salt, 0).encode())).decode()
        print("token={}".format(token))

    def sign_in(self):
        print("[+] sign in with your token.")
        token = input("> ")
        try:
            ct = unhexlify(token)
            aes = AES.new(self.key, AES.MODE_CTR, counter=Counter.new(128, initial_value=self.r))
            pt = aes.decrypt(ct).decode("latin-1").split('|')
            assert(len(pt) == 3)
            username, salt, level = pt[0], pt[1], pt[2]
            print("Welcome {}!".format(username))
            if username == self.owner and salt == self.salt and level == "1":
                print("[+] Now tell me the salt of cxlover to getflag.")
                check_salt = input("> ")
                if check_salt == self.salt:
                    print(flag)
                else:
                    print("What a shame! You seem not to be a fan of cxlover.")
                exit(0)
            else:
                print("What a shame! You seem not to be a fan of cxlover.")
        except:
            print("[!] Invalid token!")
    
def main():
    club = cxlover_club()
    club.sign_up()
    while True:
        club.sign_in()

if __name__ == '__main__':
    main()