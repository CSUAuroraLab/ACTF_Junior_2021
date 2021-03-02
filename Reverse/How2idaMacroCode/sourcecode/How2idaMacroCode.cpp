#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>

static unsigned int x = 0x114514;
static unsigned int y = 0x1919810;
#define NOT(a) (a ^ y)
#define IS(a)  (a ^ x)
//#define NOT(a) (~a)
//#define XOR0(a, b) ((a | b) & (NOT(a) | NOT(b)))
//#define XOR1(a,b) (NOT(NOT(a)&NOT(b))&NOT(a&b))
#define XOR2(a,b) ((a&NOT(b))|(NOT(a)&b))

//ACTF{sometimes_ida_is_not_reliable_READ_THE_ASM}

__attribute__((constructor)) void init_const(){
    x = 0;
    y = 0xffffffff;
}
bool check(const char*);

int main()
{
    puts("Welcome");
    puts("This is a Program,confound by Gstalker");
    puts("input");
    char *buffer = (char *)malloc(0x200);
    scanf("%200s",buffer);
    if(check(buffer)){
        puts("Success");
    }
    else{
        puts("Failed");
    }
    free(buffer);
    return 0;
}

bool check(const char* target){
    bool result = true;
    unsigned int enc[12];

    enc[0]=IS(0x2b3b303a);
    enc[1]=IS(0x6071e);
    enc[2]=IS(0x4360700);
    enc[3]=IS(0x1201);
    enc[4]=IS(0x6313e17);
    enc[5]=IS(0xa1c0007);
    enc[6]=IS(0x7133618);
    enc[7]=IS(0x303e0c00);
    enc[8]=IS(0xd1b2429);
    enc[9]=IS(0x10911);
    enc[10]=IS(0x22081b15);
    enc[11]=IS(0x646b5b56);

    unsigned int *tar = (unsigned *)malloc(strlen(target)+200);
    unsigned int len = (strlen(target) + 3) / 4;
    memset(tar,0, strlen(target) + 4);
    memcpy(tar, target, strlen(target));
    int i;
    for (i = 0; i < len - 1; ++i){
        tar[i] = XOR2(tar[i],tar[i+1]);
    }
    tar[i] = XOR2(tar[i], 0x19260817);
/*     for (i = 0; i < len ; ++i){
        printf("0x%x,", tar[i]);
    } */
    for (i = 0; i < sizeof(enc)/sizeof(unsigned) ; ++i){
        unsigned temp = XOR2(tar[i], enc[i]);
        if(temp){
            return false;
        }
    }
    return result;
}