#include<stdio.h>
#include<stdlib.h>
#include<string.h>

const char b64table[] = {"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="};

const char* b64_encode(const char* target,unsigned tar_len){
    char *tar = (char *)malloc(tar_len+3);
    char *result = (char *)malloc((tar_len / 3 + 1) * 4);
    memcpy(tar,target,tar_len);
    memset(tar+tar_len,0,3);
    unsigned i = 0, j = 0;
    for (; i <= tar_len - 1 ; i += 3, j += 4){
        unsigned coding = (tar[i+0] << 16) | (tar[i+1] << 8) | (tar[i+2]);
        for (int n = 0; n < 4; ++n){
            result[j + n] = b64table[(coding >> (18-6*n)) & 0b00111111];
        }
    }
    switch (tar_len % 3){
    case 1:
        result[j - 2] = '=';
    case 2:
        result[j - 1] = '=';
    case 0:
        result[j] = 0;
        free(tar);
    }
    return result;
}
//ACTF{Base64_is_a_tradional_coding_algorithm}
int main(){
    char buffer[0x200];
    puts("本程序使用了一种传统编码方式");
    puts("记住，不是加密");
    puts("没有密钥的东西算个锤子加密");
    puts("please Inuput");
    
    while(1){
        memset(buffer, 0, 0x200);
        scanf("%256s",buffer);
        const char* result = b64_encode(buffer, strlen(buffer));
        if(strcmp("QUNURntCYXNlNjRfaXNfYV90cmFkaW9uYWxfY29kaW5nX2FsZ29yaXRobX0=",result)==0){
            puts("Success!");
            break;
        }
        else{
            puts("failure!");
        }
    }
    system("pause");
    return 0;
}