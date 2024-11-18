from Crypto.Util.number import getPrime, isPrime, inverse
from hashlib import sha256
from random import randint

class Elgamal:
	def __init__(self):
		self.q, self.g = self.gen()
		self.d = randint(0, self.q - 2)
		self.y = pow(self.g, self.d, self.q)

	def gen(self): 
		#原根生成函数
		q = 8867984692712162589394753592684462893849721383808359270870591946309591420901509987341888487540800853389811701998166292427185543648905432008953442556844003
		
		while True:
			#q = getPrime(512)
			p = 2*q + 1
			if isPrime(p):
				g = randint(2,p-1)
				if (pow(g,2,p) != 1) & (pow(g,q,p) != 1):
					break
		return q,g

	def Hash(self, msg): 
		#哈希函数
		return int(sha256(msg).hexdigest(),16)

	def Sign(self, msg): 
		#签名函数
		m = self.Hash(msg)
		phi = self.q - 1

		while True:
			k = getPrime(512)
			if k < phi : break

		r = pow(self.g, k, self.q)
		s = ((m - self.d * r) * inverse(k,phi)) % (phi)
		return (r,s)

	def Verity(self, msg, Signature):
		#验签函数
		m = self.Hash(msg)
		r,s = Signature

		A = (pow(self.y, r, self.q) * pow(r, s, self.q)) % self.q
		B = pow(self.g, m, self.q)

		if A == B:
			return True
		else:
			return False