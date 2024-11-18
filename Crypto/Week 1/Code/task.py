#How to use mathematics to represent information?
from Crypto.Util.number import bytes_to_long
from base64 import b64encode
#from secret import flag
flag = '0xGame{123}'
msg = flag.encode()
length = len(msg)

assert length%4 == 0
block = length//4
m = [ msg[ block*(i) : block*(i+1) ] for i in range(4) ]

m0 = m[0]
m1 = bytes_to_long(m[1])
m2 = m[2].hex()
m3 = b64encode(m[3])

print(f'm0 = {m0}\nm1 = {m1}\nm2 = {m2}\nm3 = {m3}')
'''
m0 = b'0xGame{73d7'
m1 = 60928972245886112747629873
m2 = 3165662d393339332d3034
m3 = b'N2YwZTdjNGRlMX0='
'''