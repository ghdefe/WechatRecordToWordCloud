# 微信聊天记录生成特定图片图云

## 提取聊天记录到csv参考教程
https://github.com/Heyxk/notes/issues/1
## 项目说明

该项目根据微信聊天记录，使用jieba分词后，利用wordcloud生成对应的词云。


词云形状颜色可以根据自定义图片生成，因此，该词云缩小了看是一个低分辨率图片。


若要生成图片词云，应赋值使得图云最大字号不能过大，否则将会影响显示效果，并且要制定wordcloud某个值（记不清了），使得生成的词云分辨率放大后足够看到每一个小字

# WordCloud这个包安装可能会报错

需要下载whl文件来安装，可以解决大部分问题


## 报错
>Command "python setup.py egg_info" failed with error code 1 in C:\Users\chen\AppData\Local\Temp\pip-build-cbf83t8_\matplotlib\
You are using pip version 8.1.1, however version 20.0.2 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

## 原因
这个，原因是wordcloud依赖包matplotlib找不到对应版本的安装包，下载对应版本的whl文件来安装成功结局。

## 解决方法
到下面附的镜像源下载对应版本的whl文件，然后cd到文件所在目录，pip intall就行

### 附whl文件清华镜像源
https://pypi.tuna.tsinghua.edu.cn/simple/matplotlib/