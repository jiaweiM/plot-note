# Content
- [Content](#content)
- [Artist](#artist)
- [Axes](#axes)
  - [bar](#bar)
  - [stem](#stem)
  - [set_xlabel, set_ylabel](#setxlabel-setylabel)
- [Axis](#axis)
  - [Axis.get_label_position](#axisgetlabelposition)
  - [subplots_adjust](#subplotsadjust)
- [pyplot](#pyplot)
  - [bar](#bar-1)
  - [figure](#figure)
  - [xlabel](#xlabel)
  - [pyplot.subplots](#pyplotsubplots)
  - [suptitle(t, **kwargs)](#suptitlet-kwargs)

# Artist
`Artist` 是渲染到 `FigureCanvas` 的所有元素的基类。

![](images/2019-09-05-19-41-42.png)

# Axes
https://matplotlib.org/api/axes_api.html

## bar
创建条形图。



## stem
```py
Axes.stem(self, *args, linefmt=None, markerfmt=None, basefmt=None, bottom=0, label=None, use_line_collection=False, data=None)
```

创建茎图。

茎图对每个 x 位置绘制一条垂直线到到对应的 y，并在该绘制放置一个标记。调用方式：
```py
stem([x,] y, linefmt=None, markerfmt=None, basefmt=None)
```

其中 x 位置是可选的。

## set_xlabel, set_ylabel
设置 x 或 y 轴的标签。
```py
set_xlabel(self, xlabel, fontdict=None, labelpad=None, **kwargs)
set_ylabel(self, ylabel, fontdict=None, labelpad=None, **kwargs)
```

|参数|说明|
|---|---|
|xlabel, ylabel|标签|
|labelpad|标签和边框（axes 包含刻度和刻度标签的边框）的像素距离，默认为 None|
|**kwargs|`Text` 属性值，用于设置标签格式|

# Axis

## Axis.get_label_position
获得 label 的位置（top or bottom）。

```
Axis.set_label_coords
```
设置 label 的坐标。默认 y label 的 x 坐标值由 tick label 的边框确定，如果有多个 axes，可能导致 y label 没对齐。x label 的 y 坐标值同理。



## subplots_adjust
```py
subplots_adjust(self, left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
```
通过 *kwargs* 更新 `SubplotParams`，并同时更新 subplot 的位置。

# pyplot
[`pyplot` reference](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot)

## bar
绘制条形图。

```py
pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
```
条带的位置为 x，形状大小由 width 和 height 指定，垂直的基线为 bottom（default=0）。

x, height, width, bottom 可以为标量值，应用于所有条带，也可以是长度为 N 的序列，为每个条带单独提供值。

|参数|说明|
|---|---|
|x|标量序列，用于指定条带的位置|
|height	|标量或标量序列，用于指定条带的高度|
|width	|标量或数组对象，用于指定条带宽度（default=0.8）|
|bottom	|标量或数组，条带 y 开始的位置（default=0）|
|align	|条带和 x 位置对齐的方式|   

**align**  
{"center", "edge"}
- 'center', 条带中心和 x 轴对应位置对齐
- 'edge', 条带左边和 x 轴对应位置对齐
- 如果要右边对齐，将 align 设置为 'edge'，然后将 width 设置为负数

**返回值**

`BarContainer`, 包括所有条带和 errorbars （可选）的容器。
其他参数：
xerr, yerr：标量或数组对象（shape(N) 或 shape(2,N)
	如果非空，为条带添加 errorbar
- 标量值，所有条带相同的对称的 +/- values 的 errorbar
- shape(N), 为各个条带分别指定对称的 +/- values 的 errorbar
- shape(2, N), 为各个条带指定非对称的 +/- errorbar,第一行为 lower errors, 第二行为 upper errors.
- None, 没有 errorbar  (default)

## figure
创建一个 figure.

```py
pyplot.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)
```

**figsize**

(float, float), optional, default: None.

宽度和高度的像素值。默认为 `rcParams["figure.figsize"] = [6.4, 4.8] = [6.4, 4.8]`

## xlabel
设置 x 轴的标签。

```py
pyplot.xlabel(xlabel, fontdict=None, labelpad=None, **kwargs)
```

|参数|类型|说明|
|---|---|---|
|xlabel|str|标签|
|labelpad|scalar|optional, default: None，和包含刻度和刻度标签的axes边框的距离，像素值|
|**kwargs|`Text` 属性值|用于设置标签的格式|

## pyplot.subplots
创建一个 figure 以及一系列的 subplots.

该方法用于创建 subplots 布局的 figure 特别方便。
```py
subplots(nrows=1, ncols=1, sharex=False, sharey=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)
```

|参数|类型|默认值|说明|
|---|---|---|---|
|nrows, ncols|int|1|subplot 网格行和列数|
|sharex, sharey|bool or {'none', 'all', 'row', 'col'}|false|坐标轴的共享设置|
|squeeze|bool|true|额外的维度从返回的 Axes 数组中移除|

**sharex, sharey**

值为 bool 或 {'none', 'all', 'row', 'col'}，默认为false; x 或 y 轴的共享设置。
|值|效果|
|---|---|
|True or 'all'|所有 subplots 共享 x 或 y 轴|
|False or 'none'|所有的 subplot 的坐标轴互相独立|
|'row'|每一行的 subplot 共享 x 或 y 轴|
|'col'|每一列的 subplot 共享 x 或 y 轴|

说明：
- 当多个 subplots 共享 x-axis, 只有最下面的 subplot 创建 x tick labels。
- 类似的，对共享 y-axis 的 subplots，只有第一列的 subplot 创建 y tick labels。
- 后面要启用其他 subplots 的 ticklabels，可以使用 `tick_params`。

**squeeze**

; bool; True; 
True, 额外的维度从返回的 Axes 数组中移除
	· 如果只创建一个一个 subplot，则以标量的形式返回一个 Axes 对象
	· 对 Nx1 和 1xM subplots，返回包含 Axes 对象的 1D numpy 数组。
	· 对 NxM subplots，且 N>1, M>1，则返回 2D 数组。
False, 没有任何移除操作，返回的对象总是 2D 数组，即使是 1x1 的数组。
~ num; integer or string; None; `pyplot.figure` 的关键字，用于设置 figure 的编号或 label。
~ subplot_kw; dict; 传递给 `Figure#add_subplot` 的关键字参数，用于创建 subplot
~ gridspec_kw; dict; 传递给 `gridspec.GridSpec` 构造函数的关键字参数
~ **fig_kw: 用于传递给 figure() 方法的额外参数。具体可设置项可以参考 pyplot.figure()。
返回：
fig; matplotlib.figure.Figure 对象。
ax; Axes 对象或 Axes 对象数组。返回的 ax 数组的大小可以通过 squeeze 控制。


## suptitle(t, **kwargs)
为 figure 添加居中标题。

|参数|类型|默认值|说明|
|---|---|---|---|
|t|str||标题文本|
|x|float|0.5|标题在坐标系中的  x 值 |
|y|float|0.98|标题在坐标系中的 y 值|
|horizontalalignment, ha|{'center', 'left', right'}|'center'|标题文本相对坐标 (x,y) 水平对齐方式|
|verticalalignment, va|{'top', 'center', 'bottom', 'baseline'}|'top'|标题文本相对坐标 (x,y) 垂直对齐方式|
|fontsize, size||rcParams["figure.titlesize"] = 'large'|文本大小|
