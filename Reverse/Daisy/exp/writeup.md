# Daisy

`ACTF{sddddwussaaaaslddddddwwwudddlssusslaausslaaaaaaaussslddwudddddlsdud}`

## 解题思路

用ida打开后，反编译main函数

![image-20210129102232814](wppics/image-20210129102232814.png)

红框中的函数无法反编译。

![image-20210129102254352](wppics/image-20210129102254352.png)

在左侧函数列表中找到该函数，于汇编窗口中查看病灶

发现花指令，干扰了反编译器。

![image-20210129102353986](wppics/image-20210129102353986.png)

左上角：edit->patch program->assemble

填入`nop`,把红框中的指令全部覆盖掉

![image-20210129102523244](wppics/image-20210129102523244.png)

之后即可正常反编译。



![image-20210129102614543](wppics/image-20210129102614543.png)

接着是逆向。捋清楚程序逻辑之后可以发现这是一个迷宫题。

玩家出生在0，0，0这个坐标，迷宫高2层，长宽都是10。

目标是走到迷宫的D点

![image-20210129102817249](wppics/image-20210129102817249.png)

可能需要一些预处理。不过用python也好，用C语言也好，这种字符串处理对于程序员而言十分简单。

![](wppics/image-20210129102842596.png)

捋清楚路径之后，输入ACTF{路径}，就可以看到success字样

![image-20210129103141185](wppics/image-20210129103141185.png)