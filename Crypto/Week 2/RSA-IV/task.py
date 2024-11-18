#!/usr/local/bin/python
from os import urandom
from hashlib import sha256
from random import choice, getrandbits
from string import ascii_letters, digits

from challenge import *
from secret import flag

def proof_of_work():
	proof = ''.join([choice(ascii_letters+digits) for _ in range(20)])
	_hexdigest = sha256(proof.encode()).hexdigest()
	print(f"[+] sha256(XXXX+{proof[4:]}) == {_hexdigest}")
	x = input('[+] Plz tell me XXXX: ')
	if len(x) != 4 or sha256( (x+proof[4:]).encode() ).hexdigest() != _hexdigest:
		return False
	return True

def choice_(num):
	if num not in [0,1,2,3]:return
	global scores
	m = getrandbits(96)

	match num:
		case 0:
			print( challenge0(m) )
		case 1:
			print( challenge1(m) )
		case 2:
			print( challenge2(m) )
		case 3:
			print( challenge3(m) )

	print('[+] input answer:')
	m_= int(input('>'))
	scores[num] = (m_==m)
	score_= sum(scores)
	print(f'[+] score:{score_}')

	if score_ == 4:
		print(f'[+] flag:{flag}')
		exit()

assert proof_of_work()
scores = [0, 0, 0, 0]
while True:
	print('[+] input choice:')
	choice_( int(input('>')) )

