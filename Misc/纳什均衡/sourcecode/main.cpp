#include <stdio.h>
#include <stdlib.h>
#include <time.h>
void successfun_case(int n);
void play_game(int number);
void init();
void fail_case(int dome);
void introduction();
int stochastic();
void fun();
int check(int sum,int x);
int randint = 1;
int mix=1;
int max;
//int number=0;
int win;
void successfun_case(int n){
    if(n==1){ //玩家获得了一次胜利
        win++;
        printf("Congratulations on another victory\n");
        printf("You currently have %d wins\n",win);
    }
}
void play_game(int number){
    while(number>=0)
    {
        int temp;
        printf("The current number of pebbles : %d\n",number);
        printf("You choose number : ");
        scanf("%d",&temp);
        getchar();
        if(temp<mix||temp>max){
            fail_case(1);
        }
        int chance=check(number,temp);
        number-=temp;
        if(number==0)
        {
            successfun_case(1);
            return;
        }
        int output=0;
        if (chance==1){
            output=stochastic()%10;
            if(output<mix||output>max)
                output=mix;
            printf("NPC choose number : %d\n",output);
            number-=output;
        }
        else{
            output=number%(mix+max);
            printf("NPC choose number : %d\n",output);
            number-=output;
            if(number==0){
                fail_case(2);
            }
        }
    }
    
}
void init()
{ //初始化函数
    max=stochastic()%20;
    if(max<10)max+=10;
    printf("Hello CTFer, my name is Nim\n");
    printf("This is a turn-based game\n");
    printf("Look, here's a pile of rocks\n");
    printf("Each turn each person can choose to take some stones\n");
    printf("The minimum number is %d and the maximum number is %d \n",mix,max);
    printf("You can pick any number of pebbles in this interval\n");
    printf("\n");
}
void fail_case(int dome)
{
    switch (dome)
    {
    case 1:
        printf("Your input is not up to spec\n");
        printf("Can't you read the English of this Chinese grammar?\n");
        exit(0);
        break;
    case 2:
        printf("Sorry, you're not Bash\n");
        exit(0);
        break;
    case 3:
        printf("You're not Bash and you're not CTFer\n");
        exit(0);
        break;

    default:
        break;
    }
}
void introduction()
{
    printf("It's just a simple game\n");
    printf("The game will run five times\n");
    printf("You have to make the right decision every time\n");
    init();
    printf("You're ready? (y/n) ");
    char input;
    input = getchar();
    getchar();
    if (input == 'y' || input == 'Y')
    {
        return;
    }
    if (input == 'n' || input == 'N')
    {
        fail_case(3);
        return;
    }
    fail_case(1);
}
int stochastic()
{ //产生一个关于时间的随机数
    srand((long)time(NULL));
    int temp = rand();
    randint = temp % 110;
    return randint;
}
void fun(){
    printf("GAME START\n");
    int number=stochastic();
    printf("There are %d stones in the pile at present\n",number);
    printf("You can abandon the game if you have predicted that the game is impossible to win\n");
    printf("Are you sure you want to abandon?(y/n)");
    char input=getchar();
    getchar();
    int chance=check(number,0);
    if (input == 'y' || input == 'Y')
    {
        if(chance==1)
        {
            //获胜一次
            successfun_case(1);
            return;
        }
        else{
            fail_case(2);
        }
    }
    if (input == 'n' || input == 'N')
    {
        play_game(number);
        return ;
    }
    fail_case(1);
}
int check(int sum,int x){   //返回 1 即为玩家做出了正确的选择
    int s=sum%(mix+max);
    if(s==x){
        printf("Good choice\n");
        return 1;
    }
    return 0;
}
int main() 
{
    introduction();
    for (int i = 0; i < 5; i++)
    {
        fun();
    }
    FILE *fp=fopen("flag.txt","r");
    char flag[100];
    fgets(flag,100,fp);
    printf("%s",flag);//包含文件
}