#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<windows.h>

//ACTF{SMC_Protect_Need_Your_Debug_Skill}

unsigned long long encrypt[] = {0x4e413fa75f5236f8,0x18bdf366f2db7ead,0x188f7faa7cfbbee8,0x188a7daa7ceebce8,0x189f7baa7cc1bae8,0x188f79aa7cf7b8e8,0x189c77aa7ce5b6e8,0x18a375aa7cc8b4e8,0x18a973aa7cceb2e8,0x18b871aa7cd9b0e8,0x18826faa7ce5aee8,0x18a96daa7cdface8,0x18936baa7cdeaae8,0x18a369aa7ce3a8e8,0x18be67aa7ccfa6e8,0x188865aa7ce5a4e8,0x18ae63aa7cdfa2e8,0x18ab61aa7ccfa0e8,0x189f5faa7ce59ee8,0x18a55daa7cd19ce8,0x18a05baa7cd69ae8,0xdead42aa7dc798e8,0xcdd2f113c7587ead,0xdb297877f2273b26,0x22e83def452481dd,0xdead46aa7d3c95ac,0xfdd2f117c7587ead,0x8b26f677f2233b26,0x57ad08e06ada36bd,0x4a2526a7429ef56f,0x26e83d1045240ea8,0xdead4aaa7d0c95ac,0x9635f61bff507ead,0x2ae835a9cdfd862e,0x21ddbb6b0cd4e6e5,0x556f378e4a588152,0xaea82a6722938ae8,0x46e54aaa31248152,0x2152419fbf4fc8a2,0x9a1bb177f22f3b26,0xde15b99b78e3bea8,0x2ae83de451db7ead,0xdeadbeee027495ac,0x83adbeef2a1fffe5,0xdeaffe033b932b6e,0xdead3ecb165636ad};
/* bool encrypt_function(const char *target)
{
    unsigned char enc_flag[] = {0x20, 0x22, 0x35, 0x27, 0x1a, 0x32, 0x2c, 0x22, 0x3e, 0x31, 0x13, 0xe, 0x15, 0x4, 0x2, 0x15, 0x3e, 0x2f, 0x4, 0x4, 0x5, 0x3e, 0x38, 0xe, 0x14, 0x13, 0x3e, 0x25, 0x4, 0x3, 0x14, 0x6, 0x3e, 0x32, 0xa, 0x8, 0xd, 0xd, 0x1c};
    unsigned char tar[0x50];
    for(int i = 0 ;i < 0x50 ;++i){
        tar[i] = 0;
    }
    for(int i = 0 ;i < 0x50 ;++i){
        tar[i] = target[i];
    }
    for (int i = 0; i < sizeof(enc_flag); ++i){
        tar[i] ^= 0x61;
        if(tar[i]!=enc_flag[i]){
            return false;
        }
    }
    return true;
} */

int main(){
    char buffer[0x200];
    puts("This is a program running on Linux");
    puts("Data or Code,only depend on who were executing");
    puts("Key Word:SMC");
    puts("Please Input");

    scanf("%256s", buffer);

    for (unsigned long long *i = encrypt; i < encrypt + sizeof(encrypt) - 1 ; ++i){
        *i ^= 0xdeadbeefbadb7ead;
    }
    PDWORD lpflOldProtect = (PDWORD)malloc(sizeof(DWORD));
    VirtualProtect(
        encrypt, 
        sizeof(encrypt),
        PAGE_EXECUTE,
        lpflOldProtect
    );
    

    bool (*check)(const char *);
    check = (bool(*)(const char*))encrypt;
    //if(encrypt_function(buffer)){
    if(check(buffer)){
        puts("Success");
    }
    else{
        puts("Error");
    }
    system("pause");
    VirtualProtect(
        encrypt, 
        sizeof(encrypt),
        PAGE_READWRITE,
        lpflOldProtect
    );
    free(lpflOldProtect);
    return 0;
}