#!/usr/local/bin/python
from os import urandom
from random import choice
from hashlib import sha256
from string import ascii_letters, digits

from util import *
from secret import flag

def proof_of_work():
    proof = ''.join([choice(ascii_letters+digits) for _ in range(20)])
    _hexdigest = sha256(proof.encode()).hexdigest()
    print(f"[+] sha256(XXXX+{proof[4:]}) == {_hexdigest}")
    x = input('[+] Plz tell me XXXX: ')
    if len(x) != 4 or sha256( (x+proof[4:]).encode() ).hexdigest() != _hexdigest:
        return False
    return True

if __name__ == '__main__':
    assert proof_of_work()
    KEY = urandom(8)
    keystream = RC4(KEY)

    print("[+] Give me the text you want to encrypt:")
    m = input('>')
    c = Encrypt(m,keystream)
    print("[+] Here are the encrypt result:")
    print(f'c = {c}')

    keystream = RC4(KEY)
    print("[+] Give you the encrypted flag:")
    c = Encrypt(flag,keystream)
    print(f'c = {c}')
