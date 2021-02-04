#include<stdio.h>
#include<stdlib.h>
#include<string.h>

const char flag[] = "ACTF{Welcome_to_Reversing_World}";

int main(){
    char buffer[0x200];
    puts("Welcome to ACTF Junior 2021!");
    puts("这是一道逆向入门题。题目向你索取了一条密码");
    puts("这条密码就是本题的flag。请找出他，并上传至oj");
    puts("please Input:");
    scanf("%256s",buffer);
    if(strcmp(buffer,flag)==0){
        puts("恭喜你找到了flag");
    }
    else{
        puts("请再试试");

    }
    system("pause");
    return 0;
}