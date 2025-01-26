#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<string.h>

unsigned int seed;

void init_seed() {
    int fd=open("/dev/urandom",0);
    if (fd==-1) {
        puts("open error");
        exit(0);
    }
    read(fd,&seed,4);
    close(fd);
    srand(seed);
}
void bufinit() {
    setvbuf(stdin,0,2,0);
    setvbuf(stdout,0,2,0);
    setvbuf(stderr,0,2,0);
    alarm(10);
}

int main() {
    bufinit();
    init_seed();
    int a, b, op;
    long long ans, correct_ans;
    char operators[] = {'+', '-', '*'};
    puts("Welcome to the calc game!");
    for (int i = 0; i < 100; i++) {
        a = rand() % 100; // Limit the range to avoid overflow
        b = rand() % 100; // Limit the range to avoid overflow
        op = rand() % 3; // Randomly select an operator
        printf("====Round %d====\n", i + 1);
        switch (operators[op]) {
            case '+':
                correct_ans = a + b;
                printf("%d + %d = ", a, b);
                break;
            case '-':
                correct_ans = a - b;
                printf("%d - %d = ", a, b);
                break;
            case '*':
                correct_ans = a * b;
                printf("%d * %d = ", a, b);
                break;
        }
        scanf("%lld", &ans);
        if (ans == correct_ans) {
            puts("Correct!");
        } else {
            puts("Wrong!");
            exit(0);
        }
    }
    puts("Congratulations! Here's your shell!");
    system("/bin/sh");
}
