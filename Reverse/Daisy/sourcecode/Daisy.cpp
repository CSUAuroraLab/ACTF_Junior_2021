#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>

bool check(const char *);
int maze_check(int x, int y, int z);

const char maze[] = {
    "#***#*#**#" \
    "#####*#**#" \
    "******#**#" \
    "#######***" \
    "*******###" \
    "**********" \
    "########**" \
    "**********" \
    "**#****#**" \
    "###****##*" \

    "****#*####" \
    "****#*****" \
    "#####****#" \
    "#********#" \
    "*******#*#" \
    "*******#**" \
    "#******#**" \
    "#*********" \
    "#*######**" \
    "#*******#D" \
};
//ACTF{sddddwussaaaaslddddddwwwudddlssusslaausslaaaaaaaussslddwudddddlsdud}
int main(){
    puts("这个遥遥漫长的旅途的真正意义:一切都是为了延续希望");
    puts("你会作出何种抉择？");
    char buffer[0x200];
    scanf("%s", buffer);
    if(
        !strncmp(buffer,"ACTF{",strlen("ACTF{")) && 
        check(buffer+strlen("ACTF{")) && 
        buffer[strlen(buffer)-1] == '}'
    ){
        puts("Success!");
    }
    else{
        puts("岛外会有什么事物呢?");
    }
    system("pause");
    return 0;
}

int maze_check(int x, int y, int z){
    //printf("current poi:x=%d,y=%d,z=%d\n", x, y, z);
    if(
        x<0   ||
        y<0   ||
        z<0   ||
        x>=10 ||
        y>=10 ||
        z>=2  ||
        maze[x+y*10+z*100] == '*'
    ){
        return 0;
    }
    else if(maze[x+y*10+z*100] == 'D'){
        asm(
            "mov rax,54322435566\n"\
            "add rax,624526235\n"\
            "push rax\n"\
            "push rbp\n"\
            "cmp eax,534527634\n"\
            "jz lebel2\n"\
            "sub eax,652345645\n"\
            "push rax\n"\
            "jnz lebel2\n"\
            ".byte 'U','S','E','L','E','S','S'\n"\
            "lebel2:\n"\
            "add rsp,0x18\n"\
        );
        return 1;
    }
    else{
        return 2;
    }
}

bool check(const char* target){
    char *buffer = (char*)malloc(0x200);
    memset(buffer, 0, 0x200);
    asm(
        "call lebel11\n"\
        ".byte 0xeb\n"\
        "jmp lebel12\n"\
        "lebel11:\n"\
        "inc qword ptr ss:[rsp]\n"\
        "ret\n"\
        "lebel12:\n"
    );
    memcpy(buffer, target, strlen(target));
    int x = 0, y = 0, z = 0;
    for (int i = 0; buffer[i]; i++){
        switch(buffer[i]) {
            case 'w':{
                --y;
                break;
            }
            case 's':{
                ++y;
                break;
            }
            case 'a':{
                --x;
                break;
            }
            case 'd':{
                ++x;
                break;
            }
            case 'u':{
                ++z;
                break;
            }
            case 'l':{
                --z;
                break;
            } 
            default:{
                return false;
            }
        }
        switch(maze_check(x,y,z)){
            case 0:{
                return false;
            }
            case 1:{
                return true;
            }
            case 2:{
                continue;
            }
        }
    }
    return false;
}