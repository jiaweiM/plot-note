# Content

- [Content](#content)
- [简介](#%e7%ae%80%e4%bb%8b)
- [功能说明](#%e5%8a%9f%e8%83%bd%e8%af%b4%e6%98%8e)
  - [annotate](#annotate)
  - [set_yticks](#setyticks)
  - [set_yticklabels](#setyticklabels)
  - [set_title](#settitle)
- [Ticks and tick labels](#ticks-and-tick-labels)
  - [set_xticks](#setxticks)

# 简介
`Axes` 包含 `XAxis` 和 `YAxis`，用于处理 ticks, tick labels 和 axis label 的位置和绘制。

|方法|说明|
|---|---|
|del ax.lines[0]|删除Axes.line 列表中的第一个图|
|annotate|添加注释|
|axis("")|设置坐标轴属性|
|bar()|绘制条形图|
|set_ybound()|设置 y 轴的上限和下限|
|invert_yaxis()|反转 y 轴|
|ax.legend()|添加 legend	|
|ax.lines.remove(line)|从 Axes.lines 列表中删除指定线图|
|plot()|绘制图，并添加到 Axes.lines 列表|
|set_title('title')|设置标题|
|set_xlabel("a_label")|设置 x 轴标签|
|set_ylabel("a_label")|设置 y 轴标签|
|set_xlim([min, max])|设置 x 轴数据范围|
|set_ylim([min, max])|设置 y 轴数据范围|
|set_xscale()|设置 x 轴缩放 |
|set_yscale(value, **kwargs)|设置 y 轴缩放|
|set_xticks()|设置坐标 ticks|
|set_yticks()|设置 y tick|
|set_xticklabels()|	|
|set_yticklabels()|	|
|twinx()|创建两个坐标系，共享 x 轴|

# 功能说明
## annotate
```py
annotate(s, xy, *args, **kwargs)
```
以文本 `s` 注释点 `xy`。

最简单的模式：文本放在 xy.

|参数|类型|说明|
|---|---|---|
|s|str|用于注释的文本|
|xy|(float, float)|需要注释的数据点|
|xytext|(float, float)|用于放置注释的位置，默认为xy|
|xycoords|str|Artist, Transform, tuple; xy 的坐标系，支持如下的类型：|

字符类型：
|值|描述|
|---|---|
|`figure points`|从图左下角开始的坐标|
|`figure pixels`|从图左下角开始的像素|
|`figure fraction`|从图左下角开始的比例|
|`axes points`|从 axes 左下角开始的坐标|
|`axes pixels`|从 axes 左下角开始的像素|
|`axes fraction`|从 axes 走下角开始的比例|
|`data`|使用被注释数据点的坐标系（默认）|
|`polar`|(theta, r)|

## set_yticks
```py
set_yticks(ticks, minor=False)
```
设置 yticks.

参数：
ticks, list, 在 y 轴上tick 的位置
minor, bool, False 表示设置 major ticks，True 表示设置 minor ticks

## set_yticklabels
```py
set_yticklabels(labels, fontdict=None, minor=False, **kwargs)
```
设置 y 轴的 tick labels.
labels, 字符串列表
fontdict, dict, 设置 labels 的属性，默认值：
```
{'fontsize': rcParams['axes.titlesize'],
 'fontweight': rcParams['axes.titleweight'],
 'verticalalignment': 'baseline',
 'horizontalalignment': loc}
```
minor, bool, 是否是设置 minor labels

## set_title
```py
set_title(label, fontdict=None, loc='center', pad=None, **kwargs)
```
设置 axes 的标题。



| 参数|类型|说明|
|---|---|---|
|label|str|标题文本|
|fontdict|dict|字体设置|
|loc {'center', 'left', 'right'}|str|标题位置，默认 'center'|
|pad|float|标题和 axes 顶边的距离，默认None，采用 rcParams['axes.titlepad'] 值|

`fontdict` 的默认值为：

```py
{'fontsize': rcParams['axes.titlesize'],
 'fontweight' : rcParams['axes.titleweight'],
 'verticalalignment': 'baseline',
 'horizontalalignment': loc}
```

**返回值**  
Text 对象，kwargs 为 Text 属性关键字参数。



# Ticks and tick labels

## set_xticks
设置 x 轴的刻度。
```py
Axes.set_xticks(self, ticks, minor=False)
```
|参数|类型|说明|
|ticks|list|x 轴刻度列表|
|minor|bool|False (default), 设置 major 刻度; True设置 minor 刻度|
