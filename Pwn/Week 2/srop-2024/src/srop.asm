section .data
    hello db 'Hello> '  ; 定义字符串，末尾加上换行符

section .text
    global _start                 ; 告诉链接器程序入口点

initalarm:
    mov rax, 37
    mov rdi, 30
    syscall
    ret

_start:
    call initalarm
    call repeater
    mov rax, 60
    xor rdi, rdi
    syscall

repeater:
    sub rsp, 0x50
    mov rdx, 7
    mov rsi, hello
    mov rdi, 1
    mov rax, 1
    syscall
    mov rdx, 0x400
    mov rsi, rsp
    xor rdi, rdi
    xor rax, rax
    syscall

    xor rbp, rbp
    sub rbp, 1
loop:
    inc rbp
    cmp byte  [rsp+rbp], 0
    jnz loop

    mov rdx, rbp
    mov rsi, rsp
    mov rdi, 1
    mov rax, 1
    syscall
    add rsp, 0x50
    ret
