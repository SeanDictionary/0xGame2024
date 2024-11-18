#!/usr/local/bin/python
from random import choice
from hashlib import sha256
from string import ascii_letters, digits

from util import Elgamal
from secret import flag

def proof_of_work():
    proof = ''.join([choice(ascii_letters+digits) for _ in range(20)])
    _hexdigest = sha256(proof.encode()).hexdigest()
    print(f"[+] sha256(XXXX+{proof[4:]}) == {_hexdigest}")
    x = input('[+] Plz tell me XXXX: ')
    if len(x) != 4 or sha256( (x+proof[4:]).encode() ).hexdigest() != _hexdigest:
        return False
    return True

assert proof_of_work()

S = Elgamal()
print(f'My Public Key (q,g,y):{S.q, S.g, S.y}')
msg = (b'Welcome_to_0xGame2024_Crypto').hex()

print(f'The input msg : {msg}')
msg = bytes.fromhex(msg)
r,s = S.Sign(msg)
print(f'And the msg signatue (r,s):{r,s}')

print("Now, it's your turn to help me sign something")
msg_ = bytes.fromhex(input('[+] Give me your message:\n>'))
r_ = int(input('[+] Give me your r:\n>'))
s_ = int(input('[+] Give me your s:\n>'))

if S.Verity(msg_,(r_,s_)) and (msg_ == msg):
	print("It looks like you know how to verify the signature. Try getting the flag.")
elif S.Verity(msg_,(r_,s_)):
	print(f'flag : {flag}')
else:
	print('Is something wrong ?')
