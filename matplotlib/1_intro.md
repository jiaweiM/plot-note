# Introduction

- [Introduction](#introduction)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [Figure 结构](#figure-%e7%bb%93%e6%9e%84)
    - [Figure](#figure)
    - [Axes](#axes)
    - [Axis](#axis)
    - [Artist](#artist)
  - [输入数据类型](#%e8%be%93%e5%85%a5%e6%95%b0%e6%8d%ae%e7%b1%bb%e5%9e%8b)
  - [Matplotlib & pyplot & pylab](#matplotlib--pyplot--pylab)
  - [代码风格](#%e4%bb%a3%e7%a0%81%e9%a3%8e%e6%a0%bc)
  - [后端（输出）](#%e5%90%8e%e7%ab%af%e8%be%93%e5%87%ba)
  - [性能](#%e6%80%a7%e8%83%bd)
    - [线段简化](#%e7%ba%bf%e6%ae%b5%e7%ae%80%e5%8c%96)
    - [简化标记（Marker）](#%e7%ae%80%e5%8c%96%e6%a0%87%e8%ae%b0marker)
  - [fast 样式](#fast-%e6%a0%b7%e5%bc%8f)

## 简介

[Matplotlib](https://github.com/matplotlib/matplotlib) 是一个 Python 2D 绘图库，可以生成各种出版品质的硬拷贝格式和跨平台交互式环境数据。Matplotlib 可用于 Python 脚本，Python 和 IPython shell（例如 MATLAB 或 Mathematica），Web 应用程序服务器和各种图形用户界面工具包。

Python 可视化的库很多，包括 seaborn, networkx, vispy. 大多数的库都或多或少依赖于 matplotlib。

matplotlib 大致可以分为三部分：

- matplotlib.pylab 部分提供类似于 MATLAB 图表功能的函数；
- matplotlib api 提供创建和管理图表、文本、线条、图形等；
- backends 部分则用于输出图表。

matplotlib 代码很多，初看很难使用。不过大多数 matplotlib 基本框架理解起来比较简单，入门相对容易。

matplotlib API 是分层组织的：

- 顶层是 `matplotlib.pyplot` 模块，用于添加 plot 元素（lines, images, text, etc.）到当前 figure 的当前 axes中，同 MATLAB 。
- 下一次是面向对象的接口层，这一层，`pyplot` 只用于少量位置，如创建 `figure`，然后通过 `figure` 创建 `axes`，余下的绘制任务基本由 `axes` 对象完成。
- 如果要更深层次的控制，如将 matplotlib 图嵌入到 GUI 应用，则完全抛弃 pyplot，完全使用面向对象的方法。

## Figure 结构

![figure](images/2020-04-09-17-45-50.png)

|模块|说明|
|---|---|
|Figure|整个区域，一个 figure 可以包含多个 subplots|
|Subplot|在一个 `axes` 展示的所有相关内容的区域，为 figure 的子区域，子图等效于 Axes|
|Axis|坐标轴|
|Axes|在 Matplotlib 中表示所有坐标轴组合区域，可以理解为数据绘图区域|
|Spine|数据区域的边框的四条线|
|Grid|数据区域内的线，方便数值的读取|
|Title|figure 标题|
|Axis labels|坐标轴标题，最好给出单位|
|Ticks|坐标轴上的刻度，可以有 major ticks 和 minor ticks|
|Tick labels|major 和 minor ticks 都可以标记。除了常规标记，可以指定格式，log 转换，还可|以自定义函数格式化标记|
|Legend|图例，为每个数据系列设置的标签|
|Patches|不同形状，通过 `matplotlib.patches`可以添加矩形、圆形、椭圆、环、箭头等等|

### Figure

`Figure` 为顶层容器，包含绘制的内容子图 `Axes`、一些特殊内容（titles, figure legends, etc）以及画板（canvas）。画板是实际用于绘制图表的地方，实际使用 matplotlib 种几乎完全不接触。每个 Figure 可以包含任意数目的 `Axes`，不过为 0 没有意义.

使用 `pyplot` 创建 figure：

```py
import matplotlib.pyplot as plt

fig = plt.figure()  # an empty figure with no axes
fig.suptitle("No axes on this figure")  # add a title so we know which it is

fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
```

|第一个没有 axes|第二个包含 2x2 四个 axes|
|---|---|
|![](images/fig_no_axes.png)|![](images/fig_axes4.png)|

### Axes

Axes 是 Axis 的复数，两个坐标轴组成一个二维坐标空间，每个平面图都有一个二维坐标空间，所以 matplotlib 干脆使用 `Axes` 表示一个二维图。即 `Axes` 表示子图，具有图像区域以及对应的数据空间，`Axes` 具有如下特征：

- 一个 figure 可以包含多个 `Axes`，但一个 `Axes` 对象只能在一个 `Figure` 中；
- 一个 `Axes` 包含 2 个（对3D 为 3 个）`Axis` 对象，即坐标轴，包含数据的范围；
- 通过 `Axes` 的 `set_xlim()` 和 `set_ylim()` 也可以设置坐标轴范围。
- 每个 `Axes` 包含标题`set_title()`，x 轴标签 `set_xlabel()`和 y 轴标签 `set_ylabel()`、

`Axes` 是 OO 接口的最重要的类。每个 Axes 包含 `XAixs` 和 `YAxis`，它们包括 ticks, tick locations, labels 等。

大部分绘制工作在 `Axes` 对象上进行，包括数据点、ticks、labels等内容。一般通过 subplot 函数设置 `Axes`。`Axes` 和 `Subplot` 含义相同。

### Axis

坐标轴，**数值-线**对象，用于生成坐标轴、刻度、标签和值范围等。

- 刻度的位置由 `Locator` 对象确定。
- 刻度标签由 `Formatter` 格式化。

结合使用 `Locator` 和 `Formatter` 可以精细控制刻度位置和标签。

### Artist

基本上图上的任何一个可见元素都是 `Artist` (`Figure`, `Axes`, `Axis` 等)，包括 `Text`, `Line2D`, `collection` 和 `Patch` 对象等。在渲染 figure 时，所有 artists 都被绘制到 canvas 上。

大部分 Artists 和 `Axes` 绑定，这些 Artist 不能在多个 `Axes` 中共享，也不能从一个 `Axes` 移到另一个。

## 输入数据类型

所有的绘图函数支持 `np.array` 或 `np.ma.masked_array` 类型的输入。其它类数组的对象，如 pandas 的数据对象和 `np.matrix` 部分支持。最好在绘图前将输入类型转换为 `np.array` 对象。

例如，将 `pandas.DataFrame` 转换为 `np.array`:

```py
a = pandas.DataFrame(np.random.rand(4,5), columns = list('abcde'))
a_asndarray = a.values
```

将 `np.matrix` 转换为 `np.array`:

```py
b = np.matrix([[1,2],[3,4]])
b_asarray = np.asarray(b)
```

## Matplotlib & pyplot & pylab

Matplotlib 是整个工具包，`matplotlib.pyplot` 和 `pylab` 是 matplotlib 的模块。

pyplot 模块具有当前 figure 和 axes 的概念，所有操作都作用于当前对象。`pyplot` 为面向对象 API 提供了状态机接口，状态机隐式的自动创建 figures 和 axes。

例如，`plt.plot` 创建了子图，随后所有的 `plt.plot` 都添加线条到当前子图，`plt.xlabel`, `plt.ylabel`, `plt.title` 和 `plt.legend` 设置当前子图的属性：

```py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')
plt.plot(x, x ** 2, label='quadratic')
plt.plot(x, x ** 3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title('Simple Plot')
plt.legend()

plt.show()
```

效果：

![](images/2019-09-04-20-20-13.png)

第一次调用 `plt.plot` 时自动创建了 figure 和 axes，后面调用 `plt.plot` 则利用前面创建的 axes。设置 title, legend, axis labels 也自动使用当前的 axes。

`pylab` 绑定 `matplotlib.pyplot` 和 `numpy` 同时导入，由于命名空间污染，不再推荐使用。

对非交互绘图，推荐使用 pyplot 创建 figures 然后使用 OO 接口绘图。

## 代码风格

不同人熟悉的代码风格不一，matplotlib 提供了两种官方风格。

对 pyplot 风格，顶层导入：

```py
import matplotlib.pyplot as plt
import numpy as np
```

然后调用 `np.arange`, `np.zeros`, `np.pi`, `plt.figure`, `plt.plot`, `plt.show` 等。使用 pyplot 接口创建 figures，然后使用对象方法定义 figure。面向对象 API 的最大的好处，就是清晰明了，方便重现和自定义。

## 后端（输出）

matplotlib 支持多种输出格式，每一种输出格式称为一个后端（backend）；前端（frontend）是代码。

有两种类型的后端：

- UI 后端（如 pygtk, wxpython, tkinter, qt4, macosx）,也称为交互后端。
- 硬拷贝后端，生成图片文件（PNG, SVG, PDF, PS）等，也称为无交互后端。

配置后端的方法有 4 种，如果不同配置方法存在冲突，靠后的优先。

1. `matplotlibrc` 文件中的 `backend` 参数

例如，使用配置 antigrain (agg) 渲染的 wxpython:

```py
backend: WXAgg
```

2. 设置环境变量 `MPLBACKEND`

对 Unix:
…

目前用不着，略过。

## 性能

无论是交互模式还是保存图片，都需要考虑性能问题。Matplotlib 提供了多种减少渲染时间的方法，不过会导致图的外观略微改变。减少渲染时间的方法和图的类型有关。

### 线段简化

对包含线段的图（如线图，多边形的边框等），其渲染性能可以通过 `matplotlibrc` 文件中的 `path.simplify` 和 `path.simplify_threshold` 参数控制。

- `path.simplify` 为 boolean 类型参数，表示是否简化线段。
- `path.simplify_threshold` 则设置简化多少线段，值越大，渲染越快。

如下：第一个不简化，第二个简化

```py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Setup, create data
y = np.random.rand(100000)
y[50000:] *= 2
y[np.logspace(1, np.log10(50000), 400).astype(int)] = -1
mpl.rcParams['path.simplify'] = True

mpl.rcParams['path.simplify_threshold'] = 0.0  # no simplification
plt.plot(y)
plt.show()

mpl.rcParams['path.simplify_threshold'] = 1.0  # simplification
plt.plot(y)
plt.show()
```

Matplotlib 目前默认的简化阈值为 1/9. 如果想修改默认值，修改 `matplotlibrc` 文件即可。
另外，可以对互动绘图（最大简化）和发表质量绘图（最小简化）使用不同的风格，在需要时激活。

线段简化通过将相邻的线段合并为单个矢量，之后下一个线段和当前线段的垂直距离大于 `path.simplify_threshold`。

### 简化标记（Marker）

标记也可以简化，不过没有线段稳定。标记简化只对 `Line2D` 对象有效，通过 `markevery` 属性设置。在创建 `Line2D` 时可以传入该参数，例如：

```py
plt.plot(x, y, markevery=10)
```

## fast 样式
