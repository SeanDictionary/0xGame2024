#!/usr/local/bin/python
from Cipher import BlockCipher
from secret import flag
from os import urandom

MENU = "\
+--------------+\n\
| [E] Encrypt  |\n\
| [F] Getflag  |\n\
+--------------+\n\
"

key = urandom(9)
cipher = BlockCipher(key, 4)

print(MENU)
while True:
	choice = input('[+] choice:\n>')

	if choice == 'E':
		pt = bytes.fromhex(input('[+] encrypt:\n>'))
		ct = cipher.encrypt(pt)
		print(f'[+] result: {ct.hex()}')

	if choice == 'F':
		guess = bytes.fromhex(input('[+] guess:\n>'))
		if guess == key: 
			print(f'[+] flag: {flag}')
			exit()
		else: 
			print(f'[!] Wrong')
