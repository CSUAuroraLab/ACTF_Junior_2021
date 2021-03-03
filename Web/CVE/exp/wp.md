#### [flag]

`ACTF{weblogic_rce!}`

#### [题解思路]

这题有无数种解法，本来想要出一道weblogic的未授权访问配合`ldap`达到`RCE`效果的，但因为是新生赛，也就降低到了新生的水准。直接去网上搜索你就可以看到关于`weblogic`的各种各样的`CVE`。而这些`CVE`在这个版本也基本上都可以使用。跟着`vulhub`做一遍，你就知道怎么拿到flag了。

![image-20210226171244647](https://i.loli.net/2021/02/26/HZTGqB75kgVez1w.png)

顺带一提，如果你想用`weak_password`做的话，`weblogic@welcome1`可以直接登录，这里连保护都没有开。