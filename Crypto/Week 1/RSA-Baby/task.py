from Crypto.Util.number import bytes_to_long, getPrime
from hashlib import md5
from random import randint
from gmpy2 import invert,gcd

#Hash Function:
def MD5(m):return md5(str(m).encode()).hexdigest()

#RSA AlgorithmParameter Generation Function:
def KeyGen():
	Factor_BitLength = 30
	q = getPrime(Factor_BitLength)
	p = getPrime(Factor_BitLength)
	N = p * q
	#Euler's totient function:
	phi = (p-1) * (q-1)

	#Generate Keys:
	while True:
		e = randint(1,phi)
		if gcd(e,phi) == 1:
			d = int(invert(e,phi))
			break

	#Generate Result:
	Pub_Key = (N,e)
	Prv_Key = (N,d)
	return Pub_Key,Prv_Key

Pub,Prv = KeyGen()

N = Pub[0]
e = Pub[1]
d = Prv[1]

#RSA Encrypt:
m = randint(1,N)
c = pow(m,e,N)

print(f'Pub_Key = {Pub}')
print(f'Prv_Key = {Prv}')
print(f'Encrypt_msg = {c}')

'''
Pub_Key = (547938466798424179, 80644065229241095)
Prv_Key = (547938466798424179, 488474228706714247)
Encrypt_msg = 344136655393256706
'''

flag = '0xGame{'+ MD5(m) +'}'