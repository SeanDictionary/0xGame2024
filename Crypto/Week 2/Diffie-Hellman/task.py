#!/usr/local/bin/python
from Crypto.Util.number import isPrime, getPrime
from string import ascii_letters, digits
from Crypto.Cipher import AES
from hashlib import sha256
from random import randint
from random import choice
from hashlib import md5
from os import urandom

from secret import flag

def MD5(m):return md5( str(m).encode() ).digest()

def gen(bit_length): 
	while True:
		q = getPrime(bit_length)
		p = 2*q + 1
		if isPrime(p):
			g = randint(2,p-1)
			if (pow(g,2,p) != 1) & (pow(g,q,p) != 1):
				break
	return q,g

def proof_of_work():
    proof = ''.join([choice(ascii_letters+digits) for _ in range(20)])
    _hexdigest = sha256(proof.encode()).hexdigest()
    print(f"[+] sha256(XXXX+{proof[4:]}) == {_hexdigest}")
    x = input('[+] Plz tell me XXXX: ')
    if len(x) != 4 or sha256( (x+proof[4:]).encode() ).hexdigest() != _hexdigest:
        return False
    return True

assert proof_of_work()

q,g = gen(128)
print(f'Share (q,g) : {q,g}')
Alice_PriKey = randint(1, q)
Alice_PubKey = pow(g, Alice_PriKey, q)
print(f'Alice_PubKey : {Alice_PubKey}')

Bob_PubKey = int( input("[+] Give me the Bob_PubKey\n> ") )
print(f'Bob_PubKey : {Bob_PubKey}')

Share_Key = pow(Bob_PubKey, Alice_PriKey, q)
Cipher = AES.new(MD5(Share_Key), AES.MODE_ECB)
ct = Cipher.encrypt(flag)
print(f'Alice tell Bob : {ct.hex()}')
