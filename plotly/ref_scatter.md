# Scatter Reference

- [Scatter Reference](#scatter-reference)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [常规属性](#%e5%b8%b8%e8%a7%84%e5%b1%9e%e6%80%a7)
  - [数据](#%e6%95%b0%e6%8d%ae)
    - [x](#x)
    - [y](#y)
  - [注释](#%e6%b3%a8%e9%87%8a)
    - [`data[type=scatter].text`](#datatypescattertext)
    - [`data[type=scatter].textposition`](#datatypescattertextposition)
    - [悬停文本](#%e6%82%ac%e5%81%9c%e6%96%87%e6%9c%ac)
  - [marker](#marker)
    - [marker 颜色](#marker-%e9%a2%9c%e8%89%b2)
      - [`symbol`](#symbol)
      - [size](#size)
      - [marker.line](#markerline)
    - [textfont](#textfont)
    - [error_x](#errorx)
    - [error_y](#errory)
    - [selectedpoints](#selectedpoints)
    - [selected](#selected)
    - [unselected](#unselected)
    - [fill](#fill)
  - [`mode`](#mode)
    - [`line`](#line)
      - [color](#color)
      - [width](#width)
      - [dash](#dash)
      - [shape](#shape)
      - [smoothing](#smoothing)
      - [simplify](#simplify)
  - [px.scatter](#pxscatter)

2020-04-20, 15:31
***

## 简介

`plotly.graph_objects.Scatter` 是一个图形对象，放在 Figure 的 `data` 列表中创建散点图。

scatter 包括了线图、散点图、文本图以及气泡图。

- 数据通过 `x` 和 `y` 设置
- 文本通过 `text` 设置，可以作为悬停显示内容，也可以作为数据注释文本
- 气泡图通过将 `marker.size` 和 `marker.color` 设置为数组实现

## 常规属性

- `data[type=scatter].name`

Type: string

trace 名称。在 legend 和悬停信息中显示。

- `data[type=scatter].visible`

Type: enum ( True | False | "legendonly" )

默认 True。

该 trace 是否可见。如果是 "legendonly"，则不绘制 trace，只显示 legend (前提是 legend 没有设置不可见)。

- `data[type=scatter].showlegend`

boolean, default True.

是否显示该 trace 的 legend。

## 数据

### x

- `data[type=scatter].x`

Type: list, numpy array, Pandas series of numbers, strings, or datetimes.

x 坐标值。

- `data[type=scatter].x0`

设置 `x` 的另一种方式。和 `dx` 一起使用，`x0` 是起点坐标，`dx` 是差值，建立 x 值的线性列表。

Type: number or categorical coordinate string.

默认 0.

- `data[type=scatter].dx`

默认 1.解释看 `x0`。

### y

- `data[type=scatter].y`

Type: list, numpy array, Pandas series of numbers, strings, or datetimes.

y 坐标。

- `data[type=scatter].y0`

设置 `y` 的另一种方式。和 `dy` 一起使用，`y0` 是起点坐标，`dy` 是差值，建立 y 值的线性列表。

Type: number or categorical coordinate string.

默认 0.

- `data[type=scatter].dy`

默认 1.

查看 `y0`。

- connectgaps

`data[type=scatter]`

Type: boolean

是否连接 gaps (如 Nan 值，缺失值)。

如果不连接，确实值会时线图前后断开。

## 注释

### `data[type=scatter].text`

Type: string or array of strings

Default: ""

设置和每个数据点 (x,y) 关联的文本。

- 如果是单个字符串，则所有数据点上出现相同的字符串。
- 如果是字符串数组，则字符串一一映射到数据点上。

如果 `hoverinfo` 包含一个 `text` flag，并且没有设置 "hovertext"，则这些文本会出现在 hover 标签中。

### `data[type=scatter].textposition`

设置 `text` 相对数据点 (x,y) 的位置。

{"top left", "top center", "top right", "middle left", "middle center", "middle right", "bottom left", "bottom center", "bottom right"}

默认 "middle center".

### 悬停文本

- `data[type=scatter].hovertext`

Type: string or array of strings.

default: ""

设置和数据点 (x,y) 关联的悬停文本。

- 如果为单个字符串，所有数据点具有相同的悬停字符串。
- 如果为字符串数组，则按照顺序映射到所有数据点。

要显示该悬停文本，`hoverinfo` 必须包含 "text" 标签。

- `data[type=scatter].hoverinfo`

Type: 标签组合。

"x", "y", "z", "text", "name，通过 "+" 进行组合，或者 "all", "none", "skip"。

例如："x", "y", "x+y", "x+y+z", "all"

默认："all"

设置悬停时显示的信息。如果设置为 `none` 或 `skip`，悬停不显示信息。不过设置为 `none` 时，点击时会触发悬停事件。

## marker

`data[type=scatter].marker`

包含如下特征的 dict。

### marker 颜色

- `data[type=scatter].marker.color`

设置 marker 颜色。

颜色或颜色数组。

也可以设置为数值数组，此时必须设置 `colorscale`。数组最小值和最大值分别映射到 `marker.cmin` 和 `marker.cmax` 的 colorscale。例如：

```py
data = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 11, 12, 13],
    mode='markers',
    marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2, 3])
)
```

- `data[type=scatter].marker.cmin`

数值。

设置 color domain 的最小值。在 `marker.color` 设置为数值数组时起作用，和 `marker.color` 值具有相同的单位，同时也要设置 `marker.cmax`。

- `data[type=scatter].marker.cmax`

数值。

设置 color domain 的最大值。在 `marker.color` 设置为数值数组时起作用，和 `marker.color` 值具有相同的单位，同时也要设置 `marker.cmin`。

- `data[type=scatter].marker.colorscale`

设置色阶（colorscale）。

仅在 `marker.color` 设置为数值数组时有效。

colorscale 包含归一化值映射到 rgb, rgba, hex, hsl, hsv 或命名颜色数组的数组。至少包含两个颜色值，即最小值（0）和最大值（1）对应的颜色。例如：`[[0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`。

通过 `marker.cmin` 和 `marker.cmax` 控制色阶在色彩空间里的范围。

另外，`colorscale` 还可以是如下调色板中的一个：

Greys,YlGnBu,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,Hot,Blackbody,Earth,Electric,Viridis,Cividis.

#### `symbol`

`data[type=scatter].marker`

设置 marker symbol 类型。

- 添加 100 等价于在 symbol 名称后添加 "-open"。
- 添加 200 等价于在 symbol 名称后添加 "-dot"。
- 添加 300 等价于在 symbol 名称后添加 "-open-dot" 或 "dot-open"。

 ( "0" | "circle" | "100" | "circle-open" | "200" | "circle-dot" | "300" | "circle-open-dot" | "1" | "square" | "101" | "square-open" | "201" | "square-dot" | "301" | "square-open-dot" | "2" | "diamond" | "102" | "diamond-open" | "202" | "diamond-dot" | "302" | "diamond-open-dot" | "3" | "cross" | "103" | "cross-open" | "203" | "cross-dot" | "303" | "cross-open-dot" | "4" | "x" | "104" | "x-open" | "204" | "x-dot" | "304" | "x-open-dot" | "5" | "triangle-up" | "105" | "triangle-up-open" | "205" | "triangle-up-dot" | "305" | "triangle-up-open-dot" | "6" | "triangle-down" | "106" | "triangle-down-open" | "206" | "triangle-down-dot" | "306" | "triangle-down-open-dot" | "7" | "triangle-left" | "107" | "triangle-left-open" | "207" | "triangle-left-dot" | "307" | "triangle-left-open-dot" | "8" | "triangle-right" | "108" | "triangle-right-open" | "208" | "triangle-right-dot" | "308" | "triangle-right-open-dot" | "9" | "triangle-ne" | "109" | "triangle-ne-open" | "209" | "triangle-ne-dot" | "309" | "triangle-ne-open-dot" | "10" | "triangle-se" | "110" | "triangle-se-open" | "210" | "triangle-se-dot" | "310" | "triangle-se-open-dot" | "11" | "triangle-sw" | "111" | "triangle-sw-open" | "211" | "triangle-sw-dot" | "311" | "triangle-sw-open-dot" | "12" | "triangle-nw" | "112" | "triangle-nw-open" | "212" | "triangle-nw-dot" | "312" | "triangle-nw-open-dot" | "13" | "pentagon" | "113" | "pentagon-open" | "213" | "pentagon-dot" | "313" | "pentagon-open-dot" | "14" | "hexagon" | "114" | "hexagon-open" | "214" | "hexagon-dot" | "314" | "hexagon-open-dot" | "15" | "hexagon2" | "115" | "hexagon2-open" | "215" | "hexagon2-dot" | "315" | "hexagon2-open-dot" | "16" | "octagon" | "116" | "octagon-open" | "216" | "octagon-dot" | "316" | "octagon-open-dot" | "17" | "star" | "117" | "star-open" | "217" | "star-dot" | "317" | "star-open-dot" | "18" | "hexagram" | "118" | "hexagram-open" | "218" | "hexagram-dot" | "318" | "hexagram-open-dot" | "19" | "star-triangle-up" | "119" | "star-triangle-up-open" | "219" | "star-triangle-up-dot" | "319" | "star-triangle-up-open-dot" | "20" | "star-triangle-down" | "120" | "star-triangle-down-open" | "220" | "star-triangle-down-dot" | "320" | "star-triangle-down-open-dot" | "21" | "star-square" | "121" | "star-square-open" | "221" | "star-square-dot" | "321" | "star-square-open-dot" | "22" | "star-diamond" | "122" | "star-diamond-open" | "222" | "star-diamond-dot" | "322" | "star-diamond-open-dot" | "23" | "diamond-tall" | "123" | "diamond-tall-open" | "223" | "diamond-tall-dot" | "323" | "diamond-tall-open-dot" | "24" | "diamond-wide" | "124" | "diamond-wide-open" | "224" | "diamond-wide-dot" | "324" | "diamond-wide-open-dot" | "25" | "hourglass" | "125" | "hourglass-open" | "26" | "bowtie" | "126" | "bowtie-open" | "27" | "circle-cross" | "127" | "circle-cross-open" | "28" | "circle-x" | "128" | "circle-x-open" | "29" | "square-cross" | "129" | "square-cross-open" | "30" | "square-x" | "130" | "square-x-open" | "31" | "diamond-cross" | "131" | "diamond-cross-open" | "32" | "diamond-x" | "132" | "diamond-x-open" | "33" | "cross-thin" | "133" | "cross-thin-open" | "34" | "x-thin" | "134" | "x-thin-open" | "35" | "asterisk" | "135" | "asterisk-open" | "36" | "hash" | "136" | "hash-open" | "236" | "hash-dot" | "336" | "hash-open-dot" | "37" | "y-up" | "137" | "y-up-open" | "38" | "y-down" | "138" | "y-down-open" | "39" | "y-left" | "139" | "y-left-open" | "40" | "y-right" | "140" | "y-right-open" | "41" | "line-ew" | "141" | "line-ew-open" | "42" | "line-ns" | "142" | "line-ns-open" | "43" | "line-ne" | "143" | "line-ne-open" | "44" | "line-nw" | "144" | "line-nw-open" )

 默认： "circle"

#### size

`data[type=scatter].marker`

Type: number or array of numbers, >= 0。

设置 marker 大小（像素），默认 6px。

如 `update_traces(marker_size=10)` 将 marker 大小设置为 10 像素。

#### marker.line

Parent: `data[type=scatter].marker`

- width

`data[type=scatter].marker.line`

设置 marker 边框线宽度（px）。number or array of numbers.

如 `update_traces(marker_line_width=2)` 将 marker 线条宽度设置为 2.

### textfont

### error_x

### error_y

### selectedpoints

### selected

### unselected

### fill

Parent: `data[type=scatter]`

Type: enumerated {"none", "tozeroy", "tozerox", "tonexty", "tonextx", "toself", "tonext"}

设置填充纯色的区域。

- Defaults to "none"

unless this trace is stacked, then it gets "tonexty" ("tonextx") if `orientation` is "v" ("h") Use with `fillcolor` if not "none".

- "tozerox" and "tozeroy"

fill to x=0 and y=0 respectively.

- "tonextx" and "tonexty"

fill between the endpoints of this trace and the endpoints of the trace before it, connecting those endpoints with straight lines (to make a stacked area graph); if there is no trace before it, they behave like "tozerox" and "tozeroy".

- "toself"

将 trace 的端点连接起来，构成一个闭合形状；如果包含 gaps，则连接每个segment。

- "tonext"

如果一个 trace 完全包含另一个 trace，填充两者之间的空间（如 consecutive contour lines）；如果前面没有 trace，其效果和 "toself" 一样。

如果一个 trace 没有包含另一个 trace，不要用 "tonext"。
Traces in a `stackgroup` will only fill to (or be filled to) other traces in the same group. With multiple `stackgroup`s or some traces stacked and some not, if fill-linked traces are not already consecutive, the later ones will be pushed down in the drawing order.

## `mode`

`data[type=scatter]`

设置 scatter trace 的绘制模式。

可用模式类型:

- "lines"
- "markers"
- "text"

这三种模式可以用 `"+"` 进行任意组合，或者为 "none"。

例如 "lines", "markers", "lines+markers", "lines+markers+text", "none"。

- 如果 `mode` 包含 "text"，则 `text` 添加到对应位置，否则以 hover 形式显示。
- 如果数据点小于20，trace 没有堆叠，则默认为 "lines+markers"
- 否则为 "lines".

例如：

```py
go.Scatter(
    x=[2, 4],
    y=[4, 8],
    mode="lines",
    line=go.scatter.Line(color="gray"),
    showlegend=False)
```

### `line`

`data[type=scatter]`

包含如下键值属性的dict。当 scatter 的 `mode="lines"` 时，用于设置 scatter 的线条属性。

#### color

`data[type=scatter].line`

线条颜色。

#### width

`data[type=scatter].line`

Type: >=0 的数值。

线条宽度（px），默认 2px。

#### dash

`data[type=scatter].line`

设置线条的虚线样式。默认 "solid"，即实线。

{"solid", "dot", "dash", "longdash", "dashdot", "longdashdot}

"dash" 表示虚线，"dot" 表示点。

或者 dash 长度列表，如 "5px,10px,2px,2px"。

#### shape

`data[type=scatter].line`

{"linear", "spline", "hv", "vh", "hvh", "vhv"}

线条的样式，默认为 "linear"，即直线。

"spline" 表示样条线；"hv" 表示水平垂直线；"hvh" 水平、垂直、水平线。

![line](images/2020-03-28-15-04-52.png)

#### smoothing

`data[type=scatter].line`

[0,1.3] 范围内的数字，默认 1.

`shape` 设置为 "spline" 才有效，设置平滑量。

- 0 表示无平滑，等效为 "linear"。

#### simplify

`data[type=scatter].line`

通过删除重合线的点来简化线。默认 True。

在过渡线中，可能需要禁用此功能，以免 SVG 路径受影响。

## px.scatter

