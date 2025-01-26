#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

char * hourai = 
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⢀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⢸\n"
"⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⣠⢻⠀⠙⢦⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⢸\n"
"⠀⠀⠀⠀⡄⠸⠀⠀⠀⣠⣥⠤⠦⠤⠄⠳⠀⠀⢀⣤⠶⡟⠛⠛⠻⠶⣼\n"
"⠀⠀⠀⣴⠇⢸⠀⡴⠉⠀⠀⠀⠀⠀⠀⠀⠀⠓⣧⠀⠀⡇⠀⠀⠀⠀⣿\n"
"⠀⠀⠀⢿⠦⠖⠀⠀⠀⢀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣇⠀⠀⠀⠀⡇\n"
"⠀⠀⠀⠀⡽⠀⠀⠂⠀⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡇⠀⠀⣸⡇\n"
"⠀⠀⠀⢰⠀⠀⢰⠀⢰⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠹⣷⡀⣠⠁⡇\n"
"⠀⠀⠀⢳⠀⠀⣸⠀⢹⠀⠀⠀⠀⠀⡇⠀⢠⠀⠀⠀⢰⠀⣿⡟⣇⠀⡇\n"
"⠀⠀⢸⣾⠀⢀⠿⢹⢸⣸⠀⠀⠀⢰⣧⠀⢰⠀⠀⠀⢸⠀⢹⠃⠈⡆⠁\n"
"⠀⠀⠀⢻⠀⢸⠀⠉⠀⢽⡄⠀⠀⡏⠘⠀⢻⣴⠀⠀⢸⠀⣼⠀⠀⠘\n"
"⠀⠀⠀⠀⣷⢸⣶⣶⣶⠀⠈⠲⢤⣇⢀⠳⢸⣿⠀⠀⢸⢠⣇⣠⡶⢋\n"
"⠀⠀⠀⠀⡟⡉⠗⠀⠀⠀⠀⠀⠀⠟⠻⣷⣄⡿⠀⠘⢸⠘⡀⠀⠀⢸\n"
"⠀⠀⠀⠀⣇⠃⢧⠀⠀⠀⠁⠉⣆⠀⠀⣀⣩⠃⠀⠎⢸⠀⠙⠀⡀⢸\n"
"⠀⠀⢀⠖⠁⠀⠿⠿⢶⣀⠳⠀⠚⠀⠀⣹⠶⠆⠀⢠⠀⠀⠀⠀⠀⠉⠉⠉⢦\n"
"⠀⣤⠀⠀⠀⣼⠀⢀⡿⢠⣿⣟⣿⢛⠟⠀⠀⡼⠶⣄⠙⡄\n"
"⡞⠘⣄⠀⠀⠀⡆⢸⠹⠾⣿⣿⣿⠇⠀⠀⠀⡇⠀⠀⠀⡏⡀⠀⠀⠀⠀⠀⡞\n"
"⢧⠀⠀⣰⣿⣴⡄⠀⠳⢤⣿⣿⠁⡄⠀⠀⠀⠙⣄⣼⣿⣿⣷⡄⢀⠀⠀⠰⠀⣠\n"
"⠀⣧⢹⣿⣿⣿⣿⣄⢀⣿⣿⣿⣏⠉⠲⠶⠶⣤⣸⣿⣿⣿⣿⡟⠀⣦⣄⣤⠴⠁\n"
"⠹⣤⡼⡟⢛⠛⠁⣠⣿⣿⣿⣿⣿⣶⣶⣶⠏⠉⠀⣿⣿⣿⣿⣿⣶⣇\n"
"⠀⠀⠀⠙⠼⣻⣿⣿⠀⠉⠉⠉⠉⡭⠉⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⡖⢃\n"
"⠀⠀⠀⢀⣾⣿⣿⣿⡀⠀⠀⠀⠋⠀⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⢼\n"
"⠀⠀⢀⣿⣿⣿⣿⣿⣿⣶⣄⣀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⣿⠀⡇\n"
"⢀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠓⠲⣤⠈⢀⠃\n"
"⢸⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠓⠀⢀⠉⠗⠁\n"
"⠈⠞⠉⠻⣿⣿⣿⠉⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⠹⢤⠊\n"
"⠀⠀⠳⣾⠋⢙⠿⢶⢀⠀⠸⡎⠛⢿⣿⣿⣿⣿⡿⠃⢸⣀⢷⡇\n"
"⠀⠀⠀⠈⠦⡯⣦⣀⣸⣀⡀⠀⣀⠴⠛⣀⣀⠔⠉⠉⠀⠀⠳⡇\n"
"⠀⠀⠀⠀⠀⣵⣠⠊⠀⠀⠀⠈\n";

void init()
{
    setvbuf(stdin, 0LL, 2, 0LL);
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stderr, 0LL, 2, 0LL);
    alarm(60);
    puts(hourai);
    puts("Welcome to Alice's doll house.");
    puts("The doll above is me ---  Hourai.");
    puts("Let me lead you to the world of PWN and dolls.\n\n");
}


void whaaaaat()
{
    puts("WOW,you've learned ret2text");
    puts("Here's your shell");
    system("/bin/sh");
    exit(0);
}

void getflag()
{
    puts("She likes the name!");
    puts("And you caught a segmentfault as well.");
    puts("So Here's your gift.");
    system("cat /flag1");
    puts("But you can't get the flag so easily");
    puts("Keep going!");
    exit(0);
}

int main()
{
    char buffer[0x20];
    init();
    signal(SIGSEGV,getflag);
    puts("Alice has made a new doll.");
    puts("What name do you want to give her:");
    gets(buffer);
    if(strlen(buffer) <= 0x27)
    {
    	puts("She may like a longer name.");
    }
    return 0;
}
