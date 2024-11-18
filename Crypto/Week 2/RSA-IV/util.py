from os import urandom
from secret import flag

def KSA(key):
    keylength = len(key)

    S = [i for i in range(256)]

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]  # swap

    return S

def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap

        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(key):
    S = KSA(key)
    return PRGA(S)

def Encrypt(plaintext,keystream):
    if type(plaintext) == bytes:
        pt = plaintext
    else:
        pt = bytes.fromhex(plaintext)

    result = b''
    for i in pt:
        result += bytes([i^next(keystream)])
    return result.hex()

if __name__ == '__main__':
    KEY = urandom(8)
    keystream = RC4(KEY)
    print("Now it's your turn")
    print("Give me the text you want to encrypt:")
    m = input('>')
    c = Encrypt(m,keystream)
    print("Here are the encrypt result:")
    print(f'c = {c}')

    keystream = RC4(KEY)
    print("Now it's my turn")
    print("Give you my encrypted text:")
    c = Encrypt(flag,keystream)
    print("Here are the encrypt result:")
    print(f'c = {c}')