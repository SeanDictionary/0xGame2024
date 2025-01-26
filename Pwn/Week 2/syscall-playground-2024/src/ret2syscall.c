#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>
#define BUFFER_SIZE 0x400
#define BUFFER_CNT 6
char *buffers[BUFFER_CNT] = {NULL};
int find_avail_buffer() {
    for (int i = 0; i < BUFFER_CNT; i++) {
        if (buffers[i] == NULL) {
            return i;
        }
    }
    return -1;
}
void bufinit() {
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);
    alarm(30);
}
int main() {
    bufinit();
    while (1) {
        printf("1. Prepare a buffer\n");
        printf("2. Recycle a buffer\n");
        printf("3. Initiate a syscall with glibc wrapper\n");
        printf("Your choice: ");
        int choice;
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            {
                int idx = find_avail_buffer();
                if (idx == -1) {
                    printf("No available buffer\n");
                } else {
                    buffers[idx] = (char *)malloc(BUFFER_SIZE);
                    printf("Buffer %d is prepared. Size: %d, located at %p\n", idx, BUFFER_SIZE, buffers[idx]);
                    printf("Input your data: ");
                    read(0, buffers[idx], BUFFER_SIZE);
                    printf("Data is stored\n");
                }
                break;
            }
        case 2:
            {
                printf("Which buffer do you want to recycle: ");
                int idx;
                scanf("%d", &idx);
                if (idx < 0 || idx >= BUFFER_CNT || buffers[idx] == NULL) {
                    printf("Invalid buffer\n");
                } else {
                    free(buffers[idx]);
                    buffers[idx] = NULL;
                    printf("Buffer %d is recycled\n", idx);
                }
                break;
            }
        case 3:
            {
                printf("Now I will initiate a syscall with glibc wrapper\n");
                printf("Which syscall do you want to call: ");
                int syscall_num;
                scanf("%d", &syscall_num);
                printf("Input the arguments count: ");
                int argc;
                scanf("%d", &argc);
                unsigned long long args[6]={0};
                memset(args, 0, sizeof(args));
                for (int i = 0; i < argc; i++) {
                    printf("Input the argument %d: ", i);
                    scanf("%llu", &args[i]);
                }
                printf("Initating syscall %d with %d arguments\n", syscall_num, argc);
                int ret=syscall(syscall_num, args[0], args[1], args[2], args[3], args[4], args[5]);
                printf("Syscall returned with code %d\n", ret);
            }
        default:
            printf("Invalid choice\n");
            break;
        }
    }
}