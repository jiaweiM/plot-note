# bar

- [bar](#bar)
  - [参考](#%e5%8f%82%e8%80%83)
    - [`data[type=bar]` 参数](#datatypebar-%e5%8f%82%e6%95%b0)
    - [`x`](#x)
    - [`y`](#y)
    - [marker](#marker)
      - [line](#line)
      - [color](#color)
      - [cauto](#cauto)
      - [cmin](#cmin)
    - [textangle](#textangle)
    - [textfont](#textfont)
    - [error_x](#errorx)
    - [error_y](#errory)
    - [meta](#meta)
  - [text](#text)
    - [`data[type=bar].text`](#datatypebartext)
    - [`data[type=bar].textposition`](#datatypebartextposition)
    - [`data[type=bar].texttemplate`](#datatypebartexttemplate)
    - [`data[type=bar].hovertext`](#datatypebarhovertext)
    - [`data[type=bar].hoverinfo`](#datatypebarhoverinfo)
    - [`data[type=bar].hovertemplate`](#datatypebarhovertemplate)

2020-04-20, 17:35
***

## 参考

### `data[type=bar]` 参数

1. `name`

trace 名称。在legend 以及鼠标在数据上悬停时显示。

3. `visible`
   - True，绘制 trace
   - False，不绘制 trace
   - "legendonly"，不绘制 trace，但 legend 可见

yongyu shehzi  trace 是否可见。

4. `showlegend`
    - default `True`

该 trace 的 legend 是否可见。

### `x`

`data[type=bar]`

list, numpy array 或 Pandas series of numbers, strings or datetimes.

设置 x 坐标。

例如：

```py
go.Bar(x=[1, 2, 3], y=[1, 3, 2])
```

或者：

```json
'data': [{'x': [1, 2, 3], 'y': [1, 3, 2], 'type': 'bar'}]
```

### `y`

`data[type=bar]`

设置 y 坐标。

使用方式同 x。

### marker

`data[type=bar].marker`

包含下面列出的一个或多个键值的字典。

#### line

`data[type=bar].marker.line`

- coloraxis

Type: subplotid.

对共享颜色轴的引用。如 "coloraxis", "coloraxis2", "coloraxis3"等。

在 layout 中设置对共享颜色轴，如 `layout.coloraxis`, `layout.coloraxis2`等。

#### color

#### cauto

#### cmin

### textangle

parent `data[type=bar]`

### textfont

parent: `data[type=bar]`

### error_x

parent: `data[type=bar]`

### error_y

parent: `data[type=bar]`

### meta

Parent: `data[type=bar]`

Type: number of categorical coordindate string

此 trace 关于文本属性的额外信息。

## text

注释文本相关设置。

### `data[type=bar].text`

注释文本。

- 单字符串，所有数据相同文本
- 字符串数组，按顺序应用于数据

如果 `hoverinfo` 包含 `text` flag，且未设置 "hovertext"，则 `text` 出现在悬停信息中。

### `data[type=bar].textposition`

enum 值：{"inside", "outside", "auto", "none"}

默认："none"

指定 `text` 的位置：

- "inside" 将 `text` 放在 bar 里面，和 bar 的末端挨着，需要时对文本进行旋转和缩放。
- "outside" 将 `text` 放在 bar 外面，和 bar 末端挨着，需要时对文本其进行缩放。如果有其它的 bar 堆叠在上面， `text` 会被压入 "inside"。
- "auto" 首先尝试将 `text` 放在里面，如果里面位置太小，外面也没有其它的 bar 堆叠，则将 `text` 移到外面。

### `data[type=bar].texttemplate`

用于渲染数据的注释文本信息模板字符串。默认 ""。**该参数会覆盖 `text`**。

Type: string or array of string.

格式说明：

- 通过 `%{variable}` 插入变量。例如 `y: %{y}`。
- 通过 d3 格式化语法 `%{variable:d3-format}` 格式化数字，例如 `Price: %{y:$.2f}`，详细信息可以参考 [d3 文档](https://github.com/d3/d3-3.x-api-reference/blob/master/Formatting.md#d3_format)。
- 通过 d3-time-format 语法 `%{variable|d3-time-format}` 格式化日期，例如 `Day: %{2019-01-01|%A}`，详细参考 [d3 文档](https://github.com/d3/d3-3.x-api-reference/blob/master/Time-Formatting.md#format)

例如：

### `data[type=bar].hovertext`

用于设置数据点的悬停信息。

- 单字符串，所有数据相同文本
- 字符串数组，按顺序应用于数据

`hoverinfo` 包含 "text" flag 才能显示。

### `data[type=bar].hoverinfo`

flag:

- "x", "y", "z", "text", "name" 通过 "+" 组合；
- 或者 "all", "none", "skip"

默认 "all"。

Examples: "x", "y", "x+y", "x+y+z", "all"

`none` 和 `skip` 不显示悬停信息，`none` 点击依然触发悬停事件。

### `data[type=bar].hovertemplate`

用于渲染数据悬停文本的模板字符串。默认 ""。**该参数会覆盖 `hoverinfo`**。

Type: string or array of string.

格式说明：

- 通过 `%{variable}` 插入变量。例如 `y: %{y}`。
- 通过 d3 格式化语法 `%{variable:d3-format}` 格式化数字，例如 `Price: %{y:$.2f}`，详细信息可以参考 [d3 文档](https://github.com/d3/d3-3.x-api-reference/blob/master/Formatting.md#d3_format)。
- 通过 d3-time-format 语法 `%{variable|d3-time-format}` 格式化日期，例如 `Day: %{2019-01-01|%A}`，详细参考 [d3 文档](https://github.com/d3/d3-3.x-api-reference/blob/master/Time-Formatting.md#format)
- `hovertemplate` 中的可用变量为 [plotlyjs-events](https://plotly.com/javascript/plotlyjs-events/#event-data) 时间数据发出的变量。
