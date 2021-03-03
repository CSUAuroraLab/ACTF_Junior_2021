## easySSRF

打开url发现直接给出了源代码。

题目提示flag在192.168.54.3。这是一个内网ip，不能直接通过浏览器访问到。但这里可以利用SSRF的漏洞来访问这个内网ip。我们传入get参数：`url=http://192.168.54.3/`，发现能够读取到这台内网机器的代码：

![image-20210215231051151](https://gitee.com/Lieutenantas/md-pic/raw/master/20210228234400.png)

我们可以轻松的利用这台内网机器上运行的web服务来执行任意代码。只需要传入的get参数为：`a=system&b=cat /flag.txt`就可以读取到flag了。但是，这里其实需要对url再进行一次URL编码，否则在curl api中会显示错误。

![image-20210215231439501](https://gitee.com/Lieutenantas/md-pic/raw/master/20210228234405.png)

> 注意这里的+号不能使用空格，原因可以自己细品一下:-)

复制URL编码后的代码到浏览器上再次访问以读取flag：

![image-20210215231639710](https://gitee.com/Lieutenantas/md-pic/raw/master/20210228234407.png)