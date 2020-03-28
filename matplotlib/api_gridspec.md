# TOC
- [TOC](#toc)
- [matplotlib.gridspec](#matplotlibgridspec)
- [matplotlib.gridspec.GridSpec](#matplotlibgridspecgridspec)
- [SubplotSpec](#subplotspec)
  - [get_geometry](#getgeometry)
  - [get_position](#getposition)

# matplotlib.gridspec
`gridspec` 模块包含以网格形式布局 figure 中多个 `Axes` 的类。

`GridSpec` 用于指定总体的网格结构，单个网格由 `SubplotSpec` 表示。

# matplotlib.gridspec.GridSpec
```py
matplotlib.gridspec.GridSpec(nrows, ncols, figure=None, left=None, bottom=None, right=None, top=None, wspace=None, hspace=None, width_ratios=None, height_ratios=None)
```
`GridSpec` 用于指定网格的结构。

|参数|类型|说明|
|---|---|---|
|nrows|int|网格的行数|
|ncols|int|网格的列数|
|figure|Figure|可选|
|left, right, bottom, right|float, optional|子图（subplot）大小，对应值为 figure 宽度和高度的比例值。Left 不能大于 right，bottom 不能大于 top|
|wspace|float, optional|子图横向间距，值为 axis 平均宽度的比例值|
|hspace|float, optional|子图纵向间距，值为 axis 平均高度的比例值|
|width_ratios|长度为 ncols的可迭代对象|指定每一列的宽度比例|
|height_ratios|长度为 nrows 的可迭代对象|指定每一行的高度比例|


# SubplotSpec
```py
matplotlib.gridspec.SubplotSpec(gridspec, num1, num2=None)
```
`SubplotSpec` 用于指定子图在 `GridSpec` 中的位置。

> 不需要手动实例化 `SubplotSpec`，一般通过 `GridSpec` item-access 获得对应实例。

|参数|类型|说明|
|---|---|---|
|gridspec|`GridSpec`|子图所在的 `GridSpec`|
|num1, num2|int|子图占据网格 num1，如果提供了 num2，则子图占据 num1 到 num2 的所有网格，索引为 0-based|

## get_geometry
```py
get_geometry(self)
```

返回子图的位置，类型为 tuple `(n_rows, n_cols, start, stop)`。

索引 `start` 和 `stop` 指定子图在 `GridSpec` 中占据的范围，`stop` 为 inclusive。

## get_position
```py
get_position(self, figure, return_all=False)
```

