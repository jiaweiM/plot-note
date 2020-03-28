# TOC
- [TOC](#toc)
- [matplotlib.figure](#matplotlibfigure)
- [figure.Figure](#figurefigure)
	- [add_axes](#addaxes)
	- [add_gridspec](#addgridspec)
	- [tight_layout](#tightlayout)
	- [suptitle](#suptitle)
- [SubplotParams](#subplotparams)
	- [update](#update)

# matplotlib.figure
该模块提供包含所有绘图元素顶层容器 Figure。

该模块包含两个类：
- SubplotParams, 控制子图间距
- Figure, 绘图元素的顶层容器

`Figure` 实例的 `CallbackRegistry`类型的 `callbacks` 属性使其支持回调。支持的事件包括 'dpi_changed'，回调通过 `func(fig)` 调用，其中 `fig` 为 `Figure` 实例。

|属性|说明|
|---|---|
|patch|表示 figure 背景 的 `Rectangle` 实例|
|suppressComposite|对包含多个 figure 的图片，figure 会根据渲染函数 `option_image_nocomposite` 函数生成复合图像。如果 *suppressComposite* 为 boolean 值，则覆盖渲染|

https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure

# figure.Figure
```py
figure.Figure(figsize=None, dpi=None, facecolor=None, edgecolor=None, linewidth=0.0, frameon=None, subplotpars=None, tight_layout=None, constrained_layout=None)[source]
```
创建 Figure。

|参数|类型|说明|
|---|---|---|
|figsize|(float, float), optional, default `None`|figure 的宽度和高度，单位英寸，如果不提供值，默认为 `rcParams["figure.figsize"] = [6.4, 4.8]`|
|dpi|integer, optional, default `None`|figure 分辨率，默认为 `rcParams["figure.dpi" = 100.0]`|
|facecolor|color spec|背景色，默认为 `rcParams["figure.facecolor"] = 'white'` = 'w'|
|edgecolor|color spec|边框色，默认为 `rcParams["figure.edgecolor"] = 'white'` = 'w'|
|linewidth|float|frame 的线条宽度|
|frameon|bool, optional, default: `True`|是否绘制 figure 的框|
|subplotpars|`SubplotParams`|Subplot 参数，如果为 None, 使用默认 `rcParams["figure.subplot.*"] = None`|
|tight_layout|bool or dict, default `rcParams["figure.autolayout"] = False`|如果为 False，使用 `subplotpars`。如果为 True，使用默认 padding 的 `tight_layout`。如果提供包含 `pad`, `w_pad`, `h_pad` 和 `rect` 关键字的 dict 参数，则覆盖默认的 `tight_layout` paddings|


## add_axes
添加 axex 到 figure.

调用方式：
```py
add_axes(rect, projection=None, polar=False, **kwargs)
add_axes(ax)
```


添加 axes 到指定位置 rect[left, bottom, width, height]，所有值都是相对 figure 的 width, height 的比例值。
kwargs 为 Axes 的参数。如果参数完全相同，则创建的坐标系也相同，可以通过 label 属性分开：
	fig.add_axes(rect, label='axes1')
	fig.add_axes(rect, label='axes2')

## add_gridspec
```py
add_gridspec(self, nrows, ncols, **kwargs)
```
以该 figure 为容器创建一个 `GridSpec`。`GridSpec` 是网格形式的布局，可以用来创建相对复杂的布局。

|参数|类型|说明|
|---|---|---|
|nrows|int|行数|
|ncols|int|列数|
|**kwargs||传递给 `GridSpec` 的关键字参数|

## tight_layout
```py
tight_layout(self, renderer=None, pad=1.08, h_pad=None, w_pad=None, rect=None)
```
自动调整 subplt 参数以获得指定的 padding。


## suptitle
```py
suptitle(self, t, **kwargs)
```
为 figure 添加居中的标题。

|参数|类型|说明|
|---|---|---|
|t|str|标题文本|
|x|float, default 0.5|标题文本的 x 坐标|
|y|float, default 0.98|标题文本的 y 坐标|
|horizontalalignment, ha|{'center', 'left', 'right'}, default 'center'|文本相对 *(x,y)* 的水平位置|
|verticalalignment, va|{'top', 'center', 'bottom', 'baseline'}, default 'top'|文本相对 *(x,y)* 的垂直位置|
|fontsize, size|default `rcParams["figure.titlesize"] = 'large'`|文本[字体大小](api_text.md#setfontsize)|
|fontweight, weight|default `rcParams["figure.titleweight"] = 'normal'`|文本[字体粗细](api_text.md#setfontweight)|

返回标题的 `Text` 实例。

# SubplotParams
```py
matplotlib.figure.SubplotParams(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
```

`SubplotParams` 类包含控制子图间距的参数。

所有的参数值都是相对 figure 宽度和高度的比例值。默认值保存在 `rcParams["figure.subplot.[name]"] = None`。

|参数|类型|说明|
|---|---|---|
|left|float|子图左边空间|
|right|float|子图右边空间|
|bottom|float|子图下面空间|
|top|float|子图上面空间|
|wspace|float|子图横线间距，为 axis 平均宽度的比例值|
|hspace|float|子图纵向间距，为 axis 平均高度的比例值|

## update
```py
update(self, left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
```

更新参数。None 表示不改变。