#include<stdio.h>
#include<stdlib.h>

void vulunable(){
    char buffer[0x200];
    puts("canary, how 2 bypass?");
    read(stdin, buffer, 0x500);
    puts(buffer);
    return;
}

void init(){
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);
    return;
}

int main(){
    init();
    puts("hello,freshman");
    vulunable();
    vulunable();
    puts("goodbyte,freshman");
    return 0;
}

__attribute__((noreturn)) void backdoor(){
    puts("wow,how do you find this");
    system("/bin/sh");
    exit(233);
}