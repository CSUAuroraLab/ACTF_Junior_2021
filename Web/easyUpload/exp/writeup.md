## easyUpload

打开链接，发现是一个文件上传的功能。选择一个文件上传：

![image-20210215220242500](https://gitee.com/Lieutenantas/md-pic/raw/master/20210228234523.png)

![image-20210215220254728](https://gitee.com/Lieutenantas/md-pic/raw/master/20210228234525.png)

在url中打开能够看到成功上传的图片：

![image-20210215220401941](https://gitee.com/Lieutenantas/md-pic/raw/master/20210228234547.png)

尝试直接上传php一句话木马，显示上传失败：

![image-20210215221151686](https://gitee.com/Lieutenantas/md-pic/raw/master/20210228234528.png)

右键查看index.html源代码发现提示。

![image-20210215220128051](https://gitee.com/Lieutenantas/md-pic/raw/master/20210228234530.png)

于是在浏览器中打开Index.php发现可以读取到源代码：

![image-20210215221000220](https://gitee.com/Lieutenantas/md-pic/raw/master/20210228234532.png)

源代码的大致内容就是如果是上传文件，则php后端会检测文件的content-type是否为这几个字段（如果不清楚建议搜索一下http文件上传的相关内容），同时会检测文件大小是否满足条件。所以这里使用burpsuite抓包来修改相应字段：

<img src="https://gitee.com/Lieutenantas/md-pic/raw/master/20210228234535.png" alt="image-20210215221516429" style="zoom:50%;" />

上传成功后用蚁剑连接，执行命令读取flag：

![image-20210215221654088](https://gitee.com/Lieutenantas/md-pic/raw/master/20210228234538.png)
