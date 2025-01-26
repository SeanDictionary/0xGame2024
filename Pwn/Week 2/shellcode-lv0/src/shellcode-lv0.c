#include<stdlib.h>
#include<string.h>
#include<stdio.h>
#include<fcntl.h>
#include<unistd.h>
#include<stddef.h>
#include<linux/seccomp.h>
#include<linux/filter.h>
#include<sys/prctl.h>
#include<linux/audit.h>
#include<linux/bpf.h>
#include<sys/types.h>
#include<sys/mman.h>

void bufinit() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
    alarm(30);
    int fd=open("/dev/urandom", O_RDONLY);
    if(fd==-1) {
        puts("Open urandom failed!");
        exit(-1);
    }
    unsigned int seed;
    read(fd, &seed, 4);
    srand(seed);
    close(fd);
}
int main() {
    bufinit();
    char *shellcode_space=mmap(0x20240000, 0x1000, PROT_READ|PROT_WRITE|PROT_EXEC, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
    printf("Show me what you want to run: ");
    read(0, shellcode_space, 0x100);
    for(int i=0; i<0x100; i++) {
        if(shellcode_space[i]==0x90) {
            puts("Why are you asksing me to do nothing?");
            exit(-1);
        }
    }
    printf("Well Im kinda lazy, so I'll randomly drop some work......\n");
    shellcode_space+=rand()%0x100;
    ((void(*)())shellcode_space)();
    return 0;
}