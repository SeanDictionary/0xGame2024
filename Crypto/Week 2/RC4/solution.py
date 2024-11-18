from string import ascii_letters, digits
from hashlib import sha256
from itertools import product
from pwn import *
#context(log_level = 'debug')

ip = '118.195.138.159' #要netcat的ip
port = 10001 #端口
io = remote(ip,port)

def proof():
	io.recvuntil(b'XXXX+')
	proof = io.recvuntil(b')')[:-1]
	io.recvuntil(b'== ')
	hash = io.recvuntil(b'\n')[:-1].decode()
	dict = ascii_letters + digits
	for word in product(dict, repeat=4):
		word = ''.join(word).encode()
		if sha256( (word+proof) ).hexdigest() == hash: break
	io.sendlineafter(b'XXXX: ',word)

proof() #交验证码
# io.interactive() #进入交互模式

payload = ('0' * 44 * 2).encode()
io.sendlineafter(b'>',payload)
io.recvuntil(b'c = ')
c = io.recvline()
io.recvuntil(b'c = ')
c_=io.recvline()
print(xor(bytes.fromhex(c.decode()),bytes.fromhex(c_.decode())))

io.close()

