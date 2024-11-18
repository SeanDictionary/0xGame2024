#!/usr/local/bin/python
from Crypto.Cipher import AES
from hashlib import md5
from Util import *

from secret import flag

def MD5(m):return md5( str(m).encode() ).digest()

assert proof_of_work()

a = 10809567548006703521
b = 9981694937346749887
p = 25321837821840919771
E = Curve(a, b, p)
G = getrandpoint(E)

print(f'[+] Share G : {G}')
a = randint(1, E.p)
A = a * G
print(f'[+] Alice_PubKey : {A}')

B_x = int( input("[+] Give me the Bob_PubKey.x\n> ") )
B   = Point(B_x, E.find_y(B_x), E)
print(f'[+] Bob_PubKey : {B}')

Share_Key = a*B
Cipher = AES.new(MD5(Share_Key.x), AES.MODE_ECB)
ct = Cipher.encrypt(flag)
print(f'[+] Alice tell Bob : {ct.hex()}')