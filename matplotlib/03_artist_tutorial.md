# 简介

使用 `Artist` 对象渲染 canvas.

matplotlib API 有三层：
- `matplotlib.backend_bases.FigureCanvas` 是绘图区域；
- `matplotlib.backend_bases.Renderer` 执行在 `FigureCanvas` 绘制的任务；
- `matplotlib.artist.Artist` 使用 `Renderer` 在 canvas 绘制。

`FigureCanvas` 和 `Renderer` 执行所有和用户界面工具（如 `wxPython`）或绘图语言（如 PostScript）交互的任务,`Artist`则处理所有的高级命令，如布置图形、文本和线段等。用户 95% 以上的时间都在使用 `Artist`。

`Artist` 有两种类型：基础类型（primitive）和容器类型（container）。基础类型指需要绘制的标准图形对象，如 `Line2D`, `Rectangle`, `Text`, `AxesImage`等；容器类型用于放置基础类型，如 `Axis`, `Axes`, `Figure`等。

标准使用流程：创建 `Figure` 实例，使用 `Figure` 创建一个或多个 `Axes` 或 `Subplot` 实例，然后使用 `Axes` 创建基础类型。

例，使用 `pyplot.figure()` 创建 `Figure` 实例，该方法便于实例化 `Figure` 并将其同用户界面或 `FigureCanvas`。
```py
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(2, 1, 1) # two rows, one columns, first plot

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * t)
line, = ax.plot(t, s, color='blue', lw=2)

plt.show()
```

输出：

![](images/artist_ex1.png)

`Axes` 大概是 matplotlib API 中最重要的类，我们大部分时候都在和它打交道。因为 `Axes` 是大部分对象的绘制区域，并且有很多（如 `plot()`, `text()`, `hist()`, `imshow()`）用于创建基础类型（`Line2D`, `Text`, `Rectangle`）的方法。

大部分人对 `Subplot` 比较熟悉，`Subplot` 是 `Axes` 的子类，以网格的形式放置 `Subplot`。如果希望以任何位置创建 `Axes`，则直接使用 `add_axes()` 方法，其参数 `[left, bottom, width, height]` 用于指定图的大小和位置。如下所示：
```py
fig2 = plt.figure()
ax2 = fig2.add_axes([0.15, 0.1, 0.7, 0.3])
```

另外：
```py
import numpy as np
t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)
line, = ax.plot(t, s, color='blue', lw=2)
```
其中 `ax` 是由 `fig.add_subplot` 创建的 `Axes` 实例（因为 `Subplot` 是 `Axes`的子类），调用 `ax.plot` 时创建了一个 `Line2D` 对象，并将其放在 `Axes.lines` 列表中。

如果后面继续调用 `ax.plot`，这些线段都会添加到该列表中，也可以通过如下两种方法从中移除线段：
```py
del ax.lines[0]
ax.lines.remove(line)  # one or the other, not both!
```

`Axes` 也包含配置 x 轴和 y 轴的 tick, tick labels 和 axis labels的方法：
```py
xtext = ax.set_xlabel('my xdata') # returns a Text instance
ytext = ax.set_ylabel('my ydata')
```

在调用 `ax.set_xlabel` 时，对应的 `Text` 实例传递给 `XAxis`。每个 `Axes` 实例包含一个 `XAxis`实例 和一个 `YAxis`实例，分别用于处理 x 轴和 y 轴的刻度、刻度标签和坐标轴标题。

