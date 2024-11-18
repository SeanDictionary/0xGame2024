from Crypto.Util.number import getPrime, inverse, bytes_to_long

def challenge0(m):
	p = getPrime(150)
	q = getPrime(150)
	N = p * q
	e = 3
	c = pow(m, e, N)
	return (N, e, c)

def challenge1(m):
	p = getPrime(64)
	q = getPrime(64)
	N = p * q
	e = 0x10001
	dp = inverse(e, p-1)
	c = pow(m, e, N)
	return (N, e, c, dp)

def challenge2(m):
	p = getPrime(64)
	q = getPrime(64)
	N = p * q
	phi = (p-1) * (q-1)
	d = getPrime(21)
	e = inverse(d, phi)
	c = pow(m, e, N)
	return (N, e, c)

def challenge3(m):
	p = getPrime(64)
	q = getPrime(64)
	N = p * q
	e = getPrime(127)
	c = pow(m, e , N)
	e_= getPrime(127)
	c_= pow(m, e_, N)
	return (N, e, c, e_, c_)