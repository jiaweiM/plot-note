# 图像教程

2022-04-10, 23:39
***

## 简介

下面介绍如何使用 Matplotlib 显示图片。

## IPython

IPython 和 Matplotlib 结合使用体验特别好，启动 IPython 后，需要连接到 GUI 事件循环。即告诉 IPython 在哪里如何显示 plots。这里使用 `%matplotlib` magic 连接到 GUI 循环。

在 Jupyter 中，一般额外添加 `inline` 参数：

```python
%matplotlib inline
````

该 magic 命令启用内联绘图，即 plot 直接在 notebook 中显示。这对交互性非常重要。对 inline 绘图，输出 plot cell 下方 cell 的命令不会影响 plot。例如，在当前 cell 创建 plot，在下方 cell 修改 colormap 

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
