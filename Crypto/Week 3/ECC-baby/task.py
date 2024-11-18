from Crypto.Util.number import getPrime
from Crypto.Cipher import AES
from secret import key, flag
from random import randint
from hashlib import md5
from Util import *

def Pad(m):
	while len(m) % 16 != 0: m += b'\x00'
	return m

def MD5(m):
	return md5(str(m).encode()).digest()

def Encrypt(E, G, P, m):
	k = randint(1,E.p)
	G_= k * G
	P_= k * P

	M = getrandpoint(E)
	C = M + P_

	Cipher = AES.new(MD5(M.x), AES.MODE_ECB)
	enc = Cipher.encrypt( Pad(m) ).hex()

	return (G_, C, enc)


p = 4559252311
a = 1750153947
b = 3464736227

curve = Curve(a, b, p)
G = getrandpoint(curve)
P = key * G

G_, C, enc = Encrypt(curve, G, P, flag)

print(f'G = {G }')
print(f'P = {P }')
print(f'G_= {G_}')
print(f'C = {C }')
print(f'enc= {enc}')

'''
G = (2909007728,1842489211)
P = (1923527223,2181389961)
G_= (1349689070,1217312018)
C = (662346568,2640798701)
enc= 29bb47e013bd91760b9750f90630d8ef82130596d56121dc101c631dd5d88201a41eb3baa5aa958a6cd082298fc18418
'''
