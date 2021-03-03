# ret2libc

两次ROP

后面附件给了libc，泄露puts的地址后算出libc的基址，执行system(‘\bin\sh’)

使用下面这张图的gadgets即可

![image-20210303173204645](wppics/image-20210303173204645.png)