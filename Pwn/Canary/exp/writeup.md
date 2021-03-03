# Canary

简单得Canary泄露与绕过。

第一次输入，输入0x209个字节即可获取canary的高7个字节

canary的低字节一定是0x00。

![image-20210303163202541](wppics/image-20210303163202541.png)

随后栈溢出到backdoor即可

![image-20210303163253514](wppics/image-20210303163253514.png)