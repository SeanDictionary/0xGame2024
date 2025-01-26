#include<stdio.h>
#include<stdlib.h>
void *ptrlist[0x10];
int sizelist[0x10];
void bufinit() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    alarm(60);
}
void menu() {
    puts("1. Add");
    puts("2. Delete");
    puts("3. Display");
    puts("4. Edit");
    puts("Enter your choice: ");
    printf(">> ");
}
int getint() {
    char buf[0x20];
    read(0, buf, 0x10);
    return atoi(buf);
}
void add() {
    printf("Enter index: ");
    int idx = getint();
    if (idx < 0 || idx > 0x10 || ptrlist[idx] != NULL) {
        puts("Invalid index!");
        return;
    }
    printf("Enter size: ");
    int size = getint();
    if (size < 0) {
        puts("Invalid size!");
        return;
    }
    ptrlist[idx] = malloc(size);
    sizelist[idx] = size;
    printf("Enter data: ");
    read(0, ptrlist[idx], size);
    puts("Done!");
}
void show() {
    printf("Enter index: ");
    int idx = getint();
    if (idx < 0 || idx > 0x10 || ptrlist[idx] == NULL) {
        puts("Invalid index!");
        return;
    }
    printf("Data: %s\n", ptrlist[idx]);
}
void delete() {
    printf("Enter index: ");
    int idx = getint();
    if (idx < 0 || idx > 0x10 || ptrlist[idx] == NULL) {
        puts("Invalid index!");
        return;
    }
    free(ptrlist[idx]);
    puts("Done!");
}
void edit() {
    printf("Enter index: ");
    int idx = getint();
    if (idx < 0 || idx > 0x10 || ptrlist[idx] == NULL) {
        puts("Invalid index!");
        return;
    }
    printf("Enter data: ");
    read(0, ptrlist[idx], sizelist[idx]);
    puts("Done!");
}
int main() {
    bufinit();
    while (1) {
        menu();
        int choice = getint();
        switch(choice) {
            case 1:
                add();
                break;
            case 2:
                delete();
                break;
            case 3:
                show();
                break;
            case 4:
                edit();
                break;
            default:
                printf("Invalid choice\n");
        }
    }
}