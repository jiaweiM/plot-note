# matplotlib.pyplot.plot

- [matplotlib.pyplot.plot](#matplotlibpyplotplot)
  - [概述](#概述)
  - [绘制带标签数据](#绘制带标签数据)
  - [绘制多组数据](#绘制多组数据)
  - [参数](#参数)

***

## 概述

```python
matplotlib.pyplot.plot(*args, scalex=True, scaley=True, data=None, **kwargs)
```

y 对 x 绘制直线或 marker。

调用签名：

```python
plot([x], y, [fmt], *, data=None, **kwargs)
plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)
```

参数 `fmt` 用来定义基本格式，如颜色、标记和线条样式。例如：

```python
plot(x, y)        # 使用默认线条样式和颜色绘制 x 和 y
plot(x, y, 'bo')  # 使用蓝色圆圈绘制 x 和 y
plot(y)           # x 为默认索引值 0..N-1
plot(y, 'r+')     # 同上，但带有红色加号
```

还可以用 Line2D 的属性作为关键字参数设置外观。Line 属性和 `fmt` 可以混用。以下两个调用产生结果相同：

```python
plot(x, y, 'go--', linewidth=2, markersize=12)
plot(x, y, color='green', marker='o', linestyle='dashed',
     linewidth=2, markersize=12)
```

当属性和 `fmt` 冲突，关键字参数优先。

## 绘制带标签数据

对标记数据（可以通过 `obj['y']` 访问数据），有一个便捷方法。在参数中不用单独提供 x 和 y，而是提供 `data`，然后给出 x 和 y 的标签：

```python
plot('xlabel', 'ylabel', data=obj)
```

支持所有可索引对象，如 `dict`, `pandas.DataFrame` 等。

## 绘制多组数据

绘制多组数据的方法有多种。

- 最直接的方法是多次调用 `plot`，例如：

```python
plot(x1, y1, 'bo')
plot(x2, y2, 'go')
```

- 如果 x 和/或 y 是 2D 数组，那么将为每列绘制一个单独的数据集。如果 x 和 y 都是 2D 数组，则 shape 必须相同。如果只有一个数组为 2D，shape 为 (N, m)，则另一个数组长度必须为 N，对 m 个数据都用该数组。

例如：

```python
x = [1, 2, 3]
y = np.array([[1, 2], [3, 4], [5, 6]])
plot(x, y)
```

等价于：

```python
for col in range(y.shape[1]):
    plot(x, y[:, col])
```

- 第三种方法是指定多组 `[x]`, `y`, `[fmt]`

```python
plot(x1, y1, 'g^', x2, y2, 'g-')
```

此时，额外的关键字参数应用于所有数据集。此外，该语法不能与 `data` 参数组合使用。

默认每条 line 根据**样式循环**（style cycle）分配一个不同的样式。`fmt` 和 line 属性参数只在需要修改默认样式时才需提供。另外，也可以使用 [rcParams["axes.prop_cycle"]](https://matplotlib.org/stable/tutorials/introductory/customizing.html?highlight=axes.prop_cycle#matplotlibrc-sample) 修改样式循环。默认样式为 `cycler('color', ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])`。

## 参数

**x, y: array-like or scalar**

数据点的 x 和  y 坐标点。

- x 可选，默认为 `range(len(y))`。
- 这些参数通常为 1D 数组。
- 也可以是标量或二维数组（此时 columns 表示单独的数据集）。
- 这些参数不能作为关键字传递。


