#include <stdio.h>
#include <unistd.h>
void print_with_delay(char *str) {
    while (*str != '\0') {
        putchar(*str);
        fflush(stdout);
        str++;
        usleep(100000);
    }
    putchar('\n');
}
void getflag(){
    int fd=open("/flag",0);
    // get file len
    int len=lseek(fd,0,2);
    // read file
    lseek(fd,0,0);
    char *buf=malloc(len+1);
    read(fd,buf,len);
    write(1,buf,len);
}
void bufinit() {
    setvbuf(stdin,0,2,0);
    setvbuf(stdout,0,2,0);
    setvbuf(stderr,0,2,0);
    alarm(30);
}
int main() {
    bufinit();
    print_with_delay("Welcome aboard, Pwner!");
    usleep(1000000);
    print_with_delay("As you has connected to this service, I'll give you the flag!");
    usleep(1000000);
    print_with_delay("Next, prepare your linux and pwntools, you'll need them later.");
    usleep(1000000);
    print_with_delay("Maybe a LITTLE bit of knowledge as well, a LITTLE.");
    usleep(1000000);
    print_with_delay("Good Luck, and have fun!");
    usleep(1000000);
    getflag();
    return 0;
}