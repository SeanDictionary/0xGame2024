#!/usr/local/bin/python
from secret import flag
from os import urandom
from Util import *

MENU = "\
+--------------+\n\
| [E] Encrypt  |\n\
| [F] Getflag  |\n\
+--------------+\n\
"

key = urandom(6)

print(MENU)
for _ in range(11):
	choice = input('[+] choice:\n>')

	if choice == 'E':
		pt = bytes.fromhex(input('[+] encrypt:\n>'))
		ct = encrypt(pt, key)
		print(f'[+] result: {ct.hex()}')

	if choice == 'F':
		guess = bytes.fromhex(input('[+] guess:\n>'))
		if guess == key: 
			print(f'[+] flag: {flag}')
			exit()
		else: 
			print(f'[!] Wrong')
