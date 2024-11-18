from string import ascii_letters, digits
from hashlib import sha256, md5
from Crypto.Cipher import AES
from itertools import product
from pwn import *

def MD5(m):return md5( str(m).encode() ).digest()

ip = '118.195.138.159' #要netcat的ip
port = 10000 #端口
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

io.recvuntil(b': (')
q, g = [int(i) for i in io.recvuntil(b')').decode()[:-1].split(',')]

io.recvuntil(b'Alice_PubKey : ')
Alice_Pub = int(io.recvline())
io.sendlineafter(b'>', str(g).encode() )

Share_Key = pow(Alice_Pub, 1, q)

Cipher = AES.new(MD5(Share_Key), AES.MODE_ECB)

io.recvuntil(b'Alice tell Bob : ')
c = io.recvline().decode()
pt = Cipher.decrypt(bytes.fromhex(c))
print(pt)

io.close()
