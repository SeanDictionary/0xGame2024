from gmpy2 import gcdext, invert
from util import Elgamal

def crt_(b,m):
    M = 1
    y = 0
    Mm_ = []

    for i in range(len(m)):M *= m[i]
    Mm = [M // m[i] for i in range(len(m))]

    for i in range(len(m)):
        _,a,_ = gcdext(Mm[i],m[i])
        Mm_.append(int(a % m[i]))
        y += (Mm[i] * Mm_[i] * b[i])
    y = y % M
    return y


Test = Elgamal()
msg = b'Welcome_to_0xGame2024_Crypto'
msg_= b'Test'

m = Test.Hash(msg)
m_= Test.Hash(msg_)
r,s = Test.Sign(msg)
print(f'm = {m}')
phi = Test.q - 1
u = (invert(m, phi)*m_) % (phi)
s_= (s*u) % phi
r_0= r*u % phi
r_1= r % Test.q

r_ = crt_([r_0,r_1],[phi,Test.q])
print(Test.Verity(msg_,(r_0,s_)))