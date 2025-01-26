from pwn import *
context(arch='amd64', os='linux', log_level='debug')
s=remote("47.97.58.52",40010)
for i in range(100):
    s.recvuntil(b"====\n")
    dat=eval(s.recvuntil(b"=")[:-1])
    print(dat)
    s.sendline(str(dat).encode())
s.sendline(b"cat flag")
s.recv()