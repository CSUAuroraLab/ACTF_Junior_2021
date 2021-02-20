#include<stdio.h>
#include<stdlib.h>

void vulunable(){
    char buffer[0x200];
    puts("No system,How 2 /bin/sh?");
    read(0, buffer, 0x500);
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
    puts("goodbyte,freshman");
    return 0;
}