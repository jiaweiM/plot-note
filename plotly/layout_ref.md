# Layout

- [Layout](#layout)
  - [Legend](#legend)
    - [showlegend](#showlegend)
  - [Title](#title)
    - [font](#font)
      - [family](#family)
  - [uniformtext](#uniformtext)
    - [showlegend](#showlegend-1)
  - [Margins](#margins)
  - [Size](#size)
    - [autosize](#autosize)
    - [width](#width)
    - [height](#height)

2020-04-18, 20:17
***

## Legend

### showlegend

Type: boolean

是否绘制 legend。如果包含 trace，并且满足以下任意条件：

- 包含两个或多个 trace
- 包含 pie trace
- 某个 trace 的`showlegend`

## Title

`layout.title`

标题相关属性。

| 属性   | 类型   | 说明     |
| ------ | ------ | -------- |
| `text` | string | 标题文本 |

### font

`layout.title.font`

#### family

HTML 字体 family，

## uniformtext

包含下面参数的 dict.

- mode

Type: {False, "hide", "show"}

如果计算的文本尺寸小于 `uniformtext.minsize` 设置的最小尺寸的处理方式。

"hide" 表示隐藏文本。

"show" 显示文本，但不进一步缩小文本。

如果 `minsize` 大于 trace 定义的字体大小，使用 `minsize`。

- minsize

默认 0。

最小文本大小。

### showlegend

parent: `layout`

Type: boolean

是否显示 legend。如果有一个 trace，并满足如下任意条件，默认为 `True`:

- 包含两个或多个 trace
- 有 pie trace
- 显式设置 `showlegend:True`

## Margins

`layout.margin`

| 键    | 默认值 | 说明                     |
| ----- | ------ | ------------------------ |
| `l`   | 80 px  | 左边距                   |
| `r`   | 80 px  | 右边距                   |
| `t`   | 100 px | 上边距                   |
| `b`   | 80 px  | 下边距                   |
| `pad` | 0 px   | 绘图区域和轴线之间的距离 |
|`autoexpand`|True|开启边距扩展计算。legend, colorbar, updatemenus, slider, axis rangeselector and rangeslider 默认运行增加边距|

## Size

### autosize

`layout`

Type: boolean

在 relayout 时是否初始化用户未定义的 layout width 或 height。

> 首次绘图时必然初始化未定义的 layout width 或 height，不管该属性是何值。

### width

`layout`

plot 宽度，默认 700 px。

至少为 10 px。

### height

`layout`

plot 高度，默认 450 px.

至少为 10 px。
