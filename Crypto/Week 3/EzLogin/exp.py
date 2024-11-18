from pwn import *
from base64 import b64encode, b64decode
from time import time
#context(log_level = 'debug')

s = time()
xor = lambda a, b: bytes([x^y for x, y in zip(a, b)])

io = remote('118.195.138.159', 10005)

io.sendlineafter(b'>', b'R')
io.sendlineafter(b'>', b'Admin')
io.recvuntil(b'[+] cookie : ')
cookie = io.recvline()[:-1]

prefix = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x00'
cookie = xor(b64decode(cookie), prefix) + b64decode(cookie)[16:]
io.sendlineafter(b'>', b'L')
io.sendlineafter(b'>', b64encode(cookie))
print(io.recvline().decode())


def Send(payload):
	io.sendlineafter(b'>', b64encode(payload))
	result = io.recvline()
	#print(result)
	if result == b'[!] Unkown Wrong\n':
		return 0
	elif result == b'[!] JSON Wrong\n':
		return 1
	elif result == b'[!] TypeError Wrong\n':
		return 1

def PaddingOracle(before,after):
	d_iv = [0 for _ in range(16)]
	dict = list(b'0123456789abcdef{}xGame-') + [i for i in range(2, 16)]
	#print(f'dict = {dict}')
	for i in range(1, 17):
		flag = 1
		Pad = [0 for _ in range(17-i)]
		if i == 1:
			Index = []
		else:
			Index = [i for _ in range(i-1)]
		Prefix = Pad + Index

		for j in dict:
			d_iv[-i] = j ^ i
			IV = bytes(xor(xor(before,d_iv), Prefix))
			payload = IV + after
			result = Send(payload)

			if result == 1:
				d_iv[-i] = j
				flag = 0
				print(i, d_iv)
				break

		if flag == 1:
			for j in dict[::-1]:
				d_iv[-(i-1)] = j ^ i
				IV = bytes(xor(xor(before,d_iv), Prefix))
				payload = IV + after
				result = Send(payload)

				if result == 1:
					d_iv[-(i-1)] = j
					print(i, d_iv)
					break

			for j in dict:
				d_iv[-i] = j ^ i
				IV = bytes(xor(xor(before,d_iv), Prefix))
				payload = IV + after
				result = Send(payload)

				if result == 1:
					d_iv[-i] = j
					flag = 0
					print(i, d_iv)
					break

	return bytes(d_iv)

def Oracle():
	io.sendlineafter(b'>', b'F')
	io.recvuntil(b'[+] Here is flag2 : ')
	enc = io.recvline()
	print(enc)
	msg = b64decode(enc)
	io.sendlineafter(b'>', b'L')
	result = b''
	BlockLength = len(msg)//16
	print(f'[+] BlockLength = {BlockLength}')
	Block = [msg[16 * i: 16 * (i+1)] for i in range(BlockLength)]
	for i in range(0,BlockLength - 1):
		print(f'[x] Procing BlockIndex : {i}')
		result += PaddingOracle(Block[i], Block[i+1])
	return result

flag2 = Oracle()
print(flag2)
io.close()
e = time()
print(f'[+] Cost : {e-s}')