from secret import flag
from os import urandom
from base64 import b64encode

def Encrypt(msg, key):
    Lenth = len(key)
    result = ''

    upper_base = ord('A')
    lower_base = ord('a')
    KEY = [ord(key.upper()[_]) - upper_base for _ in range(Lenth)]

    index = 0
    for m in msg:
        tmp_key = KEY[index%Lenth] 
        if not m.isalpha():
            result += m
            continue

        if m.isupper(): 
            result += chr(upper_base + (ord(m) - upper_base + tmp_key) % 26)
        else: 
            result += chr(lower_base + (ord(m) - lower_base + tmp_key) % 26)
        index += 1
    return result

key = b64encode(urandom(6))[:5].decode()
print(Encrypt(flag,key))

#0lCcop{oyd94092-g8mq-4963-88b6-4helrxdhm6q7}