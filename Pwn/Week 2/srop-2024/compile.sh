#!/bin/sh
nasm -f elf64 src/srop.asm -o dist/srop.o
ld -s dist/srop.o -o dist/pwn
rm dist/srop.o