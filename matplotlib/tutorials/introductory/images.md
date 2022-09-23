# Image

2022-04-10, 23:39
***

## 简介

下面介绍如何使用 Matplotlib 显示图片。

## IPython

IPython 和 Matplotlib 结合得特别好，启动 IPython 后，需要连接到 GUI 事件循环。即告诉 IPython 在哪里如何显示图标。这里使用 `%matplotlib` magic 连接到 GUI 循环。

在 Jupyter 中，则使用：

```py
%matplotlib inline
````

该 magic 命令启用内联绘图，即图表直接出现在 notebook 中。

下面使用 pyplot API 介绍显示图片功能：

```py
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
```

## 导入图片为 numpy 数组

Matplotlib 依赖于 Pillow 库载入图像数据。

下图是我们要处理的图像；

![](images/2022-04-11-00-06-17.png)

这是一张 24-bit RGB PNG 图像（R, G, B 各 8 bits）。


## 参考

- https://matplotlib.org/stable/tutorials/introductory/images.html
