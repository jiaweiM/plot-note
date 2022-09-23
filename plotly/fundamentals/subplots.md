# Subplots

- [Subplots](#subplots)
  - [Subplot with PX](#subplot-with-px)
  - [创建子图](#创建子图)
    - [横向多图](#横向多图)
    - [纵向多图](#纵向多图)
    - [多行多列](#多行多列)
  - [子图标题](#子图标题)
  - [子图注释](#子图注释)
  - [Subplot 列宽和行高](#subplot-列宽和行高)
  - [坐标轴样式](#坐标轴样式)
  - [共享坐标轴](#共享坐标轴)
    - [共享 X 轴](#共享-x-轴)
    - [共享 Y 轴](#共享-y-轴)
    - [共享颜色轴](#共享颜色轴)
  - [subplot size](#subplot-size)
  - [subplot 文本输出](#subplot-文本输出)
  - [子图坐标系类型](#子图坐标系类型)
  - [low-level API](#low-level-api)
    - [水平 subplots - low](#水平-subplots---low)
    - [共享坐标轴 - low](#共享坐标轴---low)
    - [共享 X 轴 - low](#共享-x-轴---low)
  - [make_subplots 参考](#make_subplots-参考)
    - [`rows=1`](#rows1)
    - [`cols=1`](#cols1)
    - [`shared_xaxes=False`](#shared_xaxesfalse)
    - [`shared_yaxes=False`](#shared_yaxesfalse)
    - [`start_cell='top-left'`](#start_celltop-left)
    - [`horizontal_spacing=None`](#horizontal_spacingnone)
    - [`vertical_spacing=None`](#vertical_spacingnone)
    - [`subplot_titles=None`](#subplot_titlesnone)
    - [`column_widths=None`](#column_widthsnone)
    - [`row_heights=None`](#row_heightsnone)
    - [`specs=None`](#specsnone)
    - [`insets=None`](#insetsnone)
    - [`column_titles=None`](#column_titlesnone)
    - [`row_titles=None`](#row_titlesnone)
    - [`x_title=None`](#x_titlenone)
    - [`y_title=None`](#y_titlenone)
    - [`**kwargs`](#kwargs)

2020-04-18, 21:29
****

## Subplot with PX



## 创建子图

### 横向多图

使用 `plotly.subplots` 模块中的 `make_subplots` 函数创建带有子图的 figure。

下面创建两个 `scatter` 并排的 figure。

```py
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=1, cols=2)

fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[4, 5, 6]),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=[20, 30, 40], y=[50, 60, 70]),
    row=1, col=2
)

fig.update_layout(height=600, width=800, title_text="Side By Side Subplots")
fig.show()
```

说明：子图编号以 1 开始。

![subplots](images/2020-04-18-21-32-17.png)

### 纵向多图

下面创建一个三行一列的 figure:

```py
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=3, cols=1)

fig.append_trace(go.Scatter(
    x=[3, 4, 5],
    y=[1000, 1100, 1200],
), row=1, col=1)

fig.append_trace(go.Scatter(
    x=[2, 3, 4],
    y=[100, 110, 120],
), row=2, col=1)

fig.append_trace(go.Scatter(
    x=[0, 1, 2],
    y=[10, 11, 12]
), row=3, col=1)


fig.update_layout(height=600, width=600, title_text="Stacked Subplots")
fig.show()
```

![subplots](images/2020-04-18-21-35-29.png)

### 多行多列

下面创建一个 $2\times2$ subplot 网格，每个网格包含一个 `scatter`

```py
import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(rows=2, cols=2, start_cell="bottom-left")

fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]),
              row=1, col=1)

fig.add_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 70]),
              row=1, col=2)

fig.add_trace(go.Scatter(x=[300, 400, 500], y=[600, 700, 800]),
              row=2, col=1)

fig.add_trace(go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000]),
              row=2, col=2)

fig.show()
```

`start_cell` 用于设置网格从哪开始计数：

- `top-left`，从左上角开始计数，即左上角的网格为第一个，编号 (1, 1)
- `bottom-left`，左下角开始计数，即左下角的网格为第一个，编号 (1, 1)

默认为 `top-left`。

![subplot](images/2020-04-18-21-39-57.png)

## 子图标题

通过 `make_subplots` 的 `subplot_titles` 设置 subplot 的标题。

例如：

```py
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Plot 1", "Plot 2", "Plot 3", "Plot 4"))

fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]),
              row=1, col=1)

fig.add_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 70]),
              row=1, col=2)

fig.add_trace(go.Scatter(x=[300, 400, 500], y=[600, 700, 800]),
              row=2, col=1)

fig.add_trace(go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000]),
              row=2, col=2)

fig.update_layout(height=500, width=700,
                  title_text="Multiple Subplots with Titles")

fig.show()
```

![scatter](images/2020-04-18-23-02-00.png)

## 子图注释

```py
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=1, cols=2)

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[4, 5, 6],
        mode="markers+text",
        text=["Text A", "Text B", "Text C"],
        textposition="bottom center"
    ),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(
        x=[20, 30, 40],
        y=[50, 60, 70],
        mode="markers+text",
        text=["Text D", "Text E", "Text F"],
        textposition="bottom center"
    ),
    row=1, col=2
)

fig.update_layout(height=600, width=800, title_text="Subplots with Annotations")

fig.show()
```

![scatter](images/2020-04-18-23-03-20.png)

## Subplot 列宽和行高

`make_subplots` 的 `column_widths` 参数可用于设置 columns 的相对宽度，其值为数字列表，长度与 `cols` 参数相同，在应用前归一化，以保证加和为 1.

`row_heights` 参数类似，用于设置网格的行高。

例如，创建两个并排 traces，宽度 7:3

```py
import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2, column_widths=[0.7, 0.3])

fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]),
              row=1, col=1)

fig.add_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 70]),
              row=1, col=2)

fig.show()
```

![scatter](images/2020-04-19-09-25-18.png)

## 坐标轴样式

使用 `make_subplots` 函数创建 figure 后，其坐标轴属性（title, font, range, grid style等）可以使用 `update_xaxes` 和 `update_yaxes` 方法设置。默认应用于所有 subplots，可以通过 `row` 和 `col` 参数控制被设置的 subplot。

下面创建一个 $2\times2$的网格，每个网格放一个 scatter trace，然后分别设置每个子图的坐标轴标题。

```py
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Initialize figure with subplots
fig = make_subplots(
    rows=2, cols=2, subplot_titles=("Plot 1", "Plot 2", "Plot 3", "Plot 4")
)

# Add traces
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]), row=1, col=1)
fig.add_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 70]), row=1, col=2)
fig.add_trace(go.Scatter(x=[300, 400, 500], y=[600, 700, 800]), row=2, col=1)
fig.add_trace(go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000]), row=2, col=2)

# Update xaxis properties
fig.update_xaxes(title_text="xaxis 1 title", row=1, col=1)
fig.update_xaxes(title_text="xaxis 2 title", range=[10, 50], row=1, col=2)
fig.update_xaxes(title_text="xaxis 3 title", showgrid=False, row=2, col=1)
fig.update_xaxes(title_text="xaxis 4 title", type="log", row=2, col=2)

# Update yaxis properties
fig.update_yaxes(title_text="yaxis 1 title", row=1, col=1)
fig.update_yaxes(title_text="yaxis 2 title", range=[40, 80], row=1, col=2)
fig.update_yaxes(title_text="yaxis 3 title", showgrid=False, row=2, col=1)
fig.update_yaxes(title_text="yaxis 4 title", row=2, col=2)

# Update title and height
fig.update_layout(title_text="Customizing Subplot Axes", height=700)

fig.show()
```

![scatter](images/2020-04-19-09-32-33.png)

## 共享坐标轴

### 共享 X 轴

`make_subplots` 的 `shared_xaxes` 参数可以让多个子图共享 X 轴。

`vertical_spacing` 参数用于控制子图之间的纵向间隔。

下面创建3个垂直的 subplots，共享 X 轴。使用一个很小的 vertical spacing。

```py
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=3, cols=1,
                    shared_xaxes=True,
                    vertical_spacing=0.02)

fig.add_trace(go.Scatter(x=[0, 1, 2], y=[10, 11, 12]),
              row=3, col=1)

fig.add_trace(go.Scatter(x=[2, 3, 4], y=[100, 110, 120]),
              row=2, col=1)

fig.add_trace(go.Scatter(x=[3, 4, 5], y=[1000, 1100, 1200]),
              row=1, col=1)

fig.update_layout(height=600, width=600,
                  title_text="Stacked Subplots with Shared X-Axes")
fig.show()
```

![scatter](images/2020-04-19-09-36-12.png)

### 共享 Y 轴

`make_subplots` 的 `shared_yaxes` 用于共享 Y 轴。

```py
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=2, cols=2, shared_yaxes=True)

fig.add_trace(go.Scatter(x=[1, 2, 3], y=[2, 3, 4]),
              row=1, col=1)

fig.add_trace(go.Scatter(x=[20, 30, 40], y=[5, 5, 5]),
              row=1, col=2)

fig.add_trace(go.Scatter(x=[2, 3, 4], y=[600, 700, 800]),
              row=2, col=1)

fig.add_trace(go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000]),
              row=2, col=2)

fig.update_layout(height=600, width=600,
                  title_text="Multiple Subplots with Shared Y-Axes")
fig.show()
```

设置为 True 时，同一行的 subplots 共享 Y 轴。

![scatter](images/2020-04-19-09-40-17.png)

### 共享颜色轴

使用 `coloraxis` 在多个 subplots 中共享 colorscale。

```py
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=1, cols=2, shared_yaxes=True)

fig.add_trace(go.Bar(x=[1, 2, 3], y=[4, 5, 6],
                    marker=dict(color=[4, 5, 6], coloraxis="coloraxis")),
              1, 1)

fig.add_trace(go.Bar(x=[1, 2, 3], y=[2, 3, 5],
                    marker=dict(color=[2, 3, 5], coloraxis="coloraxis")),
              1, 2)

fig.update_layout(coloraxis=dict(colorscale='Bluered_r'), showlegend=False)
fig.show()
```

![bar](images/2020-04-19-09-52-33.png)

## subplot size

`make_subplots` 的 `specs` 参数可用于配置所有 subplots。

`specs` 必须为 2 维列表，尺寸和 `rows` 和 `cols` 参数匹配。

- `specs` 的元素可以为 `None`，表示在对应网格不初始化 subplot；
- 或者为包含 subplot 选项的 dict

`colspan` 指定占据的列数，默认为 1.

下面创建一个 $2\times2$的网格，包含 3 个 subplots。

- `specs` 的 (2,1) 元素的 `colspan` 设置为 2，使其占据两个列网格。
- `specs` 的 (2,2) 元素为 `None`，因为没有 subplot 从该位置开始。

```py
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(
    rows=2, cols=2,
    specs=[[{}, {}],
           [{"colspan": 2}, None]],
    subplot_titles=("First Subplot","Second Subplot", "Third Subplot"))

fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2]),
                 row=1, col=1)

fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2]),
                 row=1, col=2)
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[2, 1, 2]),
                 row=2, col=1)

fig.update_layout(showlegend=False, title_text="Specs with Subplot Title")
fig.show()
```

![scatter](images/2020-04-19-10-10-09.png)

## subplot 文本输出

如果将 `make_subplots` 的 `print_grid` 设置为 `True`，则输出表示 subplot 网格的字符串。

例如，下面使用 `rowspan` 和 `colspan` 创建自定义的 subplots。设置 `print_grid=True` 以输出字符串。

```py
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=5, cols=2,
                    specs=[[{}, {'rowspan': 2}],
                           [{}, None],
                           [{'rowspan': 2, 'colspan': 2}, None],
                           [None, None],
                           [{}, {}]],
                    print_grid=True)
fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2], name="(1,1)"), row=1, col=1)
fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2], name="(1,2)"), row=1, col=2)
fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2], name="(2,1)"), row=2, col=1)
fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2], name="(3,1)"), row=3, col=1)
fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2], name="(5,1)"), row=5, col=1)
fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2], name="(5,2)"), row=5, col=2)

fig.update_layout(height=600, width=600, title_text="specs examples")
fig.show()
```

无需配置的地址，采用空 dict `{}`，没有 subplot 的地方，用 `None`。

在控制台输出如下内容：

```text
This is the format of your plot grid:
[ (1,1) x,y   ]  ⎡ (1,2) x2,y2 ⎤
[ (2,1) x3,y3 ]  ⎣      :      ⎦
⎡ (3,1) x4,y4           -      ⎤
⎣      :                :      ⎦
[ (5,1) x5,y5 ]  [ (5,2) x6,y6 ]
```

![scatter](images/2020-04-19-10-18-54.png)

## 子图坐标系类型

2020-05-24, 17:11

`make_subplots` 默认所有的 subplots 的坐标系是 2D 笛卡尔坐标系。对其它类型的 subplot 类型（如 scatterpolar, scattergeo等），可以通过 `specs` 参数的 `type` 设置坐标系类型。

`type` 可用选项：

| 选项       | 类型                                                       |
| ---------- | ---------------------------------------------------------- |
| 'xy'       | 二维笛卡尔坐标系，默认类型                                 |
| 'scene'    | 三维笛卡尔坐标系                                           |
| 'polar'    | 极坐标系                                                   |
| 'ternary'  | scatterternary 的三元子图                                  |
| 'mapbox'   | scattermapbox 的 Mapbox                                    |
| 'domain'   | 独立的子图类型，如 pie, parcoords, parcats 等              |
| trace type | 根据图形名称（如 "bar", "scattergeo"等）自定确定坐标系类型 |

例如：

```py
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(
    rows=2, cols=2,
    specs=[[{"type": "xy"}, {"type": "polar"}],
           [{"type": "domain"}, {"type": "scene"}]],
)

fig.add_trace(go.Bar(y=[2, 3, 1]),
              row=1, col=1)

fig.add_trace(go.Barpolar(theta=[0, 45, 90], r=[2, 3, 1]),
              row=1, col=2)

fig.add_trace(go.Pie(values=[2, 3, 1]),
              row=2, col=1)

fig.add_trace(go.Scatter3d(x=[2, 3, 1], y=[0, 0, 0],
                           z=[0.5, 1, 2], mode="lines"),
              row=2, col=2)

fig.update_layout(height=700, showlegend=False)

fig.show()
```

该例包含了四种坐标系类型。

![type](images/2020-04-19-10-26-35.png)

也可以使用 trace 类型名称，plotly 会根据 trace 名称确定 subplot 类型。下面这个例子和上例效果相同：

```py
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(
    rows=2, cols=2,
    specs=[[{"type": "bar"}, {"type": "barpolar"}],
           [{"type": "pie"}, {"type": "scatter3d"}]],
)

fig.add_trace(go.Bar(y=[2, 3, 1]),
              row=1, col=1)

fig.add_trace(go.Barpolar(theta=[0, 45, 90], r=[2, 3, 1]),
              row=1, col=2)

fig.add_trace(go.Pie(values=[2, 3, 1]),
              row=2, col=1)

fig.add_trace(go.Scatter3d(x=[2, 3, 1], y=[0, 0, 0],
                           z=[0.5, 1, 2], mode="lines"),
              row=2, col=2)

fig.update_layout(height=700, showlegend=False)

fig.show()
```

## low-level API

### 水平 subplots - low

```py
import plotly.graph_objects as go

trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[4, 5, 6]
)
trace2 = go.Scatter(
    x=[20, 30, 40],
    y=[50, 60, 70],
    xaxis="x2",
    yaxis="y2"
)
data = [trace1, trace2]
layout = go.Layout(
    xaxis=dict(
        domain=[0, 0.7]
    ),
    xaxis2=dict(
        domain=[0.8, 1]
    ),
    yaxis2=dict(
        anchor="x2"
    )
)
fig = go.Figure(data=data, layout=layout)
fig.show()
```

![scatter](images/2020-04-19-10-50-26.png)

### 共享坐标轴 - low

```py
import plotly.graph_objects as go

trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[2, 3, 4]
)
trace2 = go.Scatter(
    x=[20, 30, 40],
    y=[5, 5, 5],
    xaxis="x2",
    yaxis="y"
)
trace3 = go.Scatter(
    x=[2, 3, 4],
    y=[600, 700, 800],
    xaxis="x",
    yaxis="y3"
)
trace4 = go.Scatter(
    x=[4000, 5000, 6000],
    y=[7000, 8000, 9000],
    xaxis="x4",
    yaxis="y4"
)
data = [trace1, trace2, trace3, trace4]
layout = go.Layout(
    xaxis=dict(
        domain=[0, 0.45]
    ),
    yaxis=dict(
        domain=[0, 0.45]
    ),
    xaxis2=dict(
        domain=[0.55, 1]
    ),
    xaxis4=dict(
        domain=[0.55, 1],
        anchor="y4"
    ),
    yaxis3=dict(
        domain=[0.55, 1]
    ),
    yaxis4=dict(
        domain=[0.55, 1],
        anchor="x4"
    )
)
fig = go.Figure(data=data, layout=layout)
fig.show()
```

![subplots](images/2020-04-19-10-54-14.png)

### 共享 X 轴 - low

```py
import plotly.graph_objects as go

trace1 = go.Scatter(
    x=[0, 1, 2],
    y=[10, 11, 12]
)
trace2 = go.Scatter(
    x=[2, 3, 4],
    y=[100, 110, 120],
    yaxis="y2"
)
trace3 = go.Scatter(
    x=[3, 4, 5],
    y=[1000, 1100, 1200],
    yaxis="y3"
)
data = [trace1, trace2, trace3]
layout = go.Layout(
    yaxis=dict(
        domain=[0, 0.33]
    ),
    legend=dict(
        traceorder="reversed"
    ),
    yaxis2=dict(
        domain=[0.33, 0.66]
    ),
    yaxis3=dict(
        domain=[0.66, 1]
    )
)
fig = go.Figure(data=data, layout=layout)
fig.show()
```

![scatter](images/2020-04-19-10-56-36.png)

## make_subplots 参考

`plotly.subplots.make_subplots(rows=1, cols=1, shared_xaxes=False, shared_yaxes=False, start_cell='top-left', print_grid=False, horizontal_spacing=None, vertical_spacing=None, subplot_titles=None, column_widths=None, row_heights=None, specs=None, insets=None, column_titles=None, row_titles=None, x_title=None, y_title=None, **kwargs)`

返回 `plotly.graph_objects.Figure` 实例。

### `rows=1`

网格行数。大于 0 的 int 值。

### `cols=1`

网格列数。大于 0 的 int 值。

### `shared_xaxes=False`

boolean 或 str，默认 False。

设置 2D 笛卡尔坐标系的 subplots 共享 x 轴：

- True 或 'columns'，同一列的 subplots 共享 x 轴
- 'rows'，同一行的 subplots 共享 x 轴
- 'all'，所有的 subplots 共享 x 轴

### `shared_yaxes=False`

boolean 或 str，默认 False。

设置 2D 笛卡尔坐标系的 subplots 共享 y 轴：

- 'columns'，同一列的 subplots 共享 y 轴
- True 或 'rows'，同一行的 subplots 共享 y 轴
- 'all'，所有的 subplots 共享 y 轴

### `start_cell='top-left'`

设置起始网格的位置：

- 'top-left'，起始为左上角的网格，编号为 (1, 1)
- 'bottom-left'，起始为左下角的网格，编号为 (1, 1)

1. `print_grid=False`

boolean, 默认 False。

是否输出网格的字符串表示形式。也可以调用生成 figure 的`Figure.print_grid()` 获得相同效果。

### `horizontal_spacing=None`

float, default 0.2/cols

columns 之间的间距，为归一化值，0 到 1 之间的 float 值。

### `vertical_spacing=None`

float, default 0.3/rows

rows 之间的间距，为归一化值，0 到 1 之间的 float 值。

### `subplot_titles=None`

str 列表或 `None`。

用于设置 subplots 的标题，按行分配。

如果某个 subplot 不想要标题，可以用空字符串 `""` 代替。

### `column_widths=None`

数字列表，长度和 `cols` 值相同。或者为 `None`。

网格列的相对宽度。在应用前会归一化，使得加和为 1。

### `row_heights=None`

数字列表，长度和 `rows` 值相同。或者为 `None`，默认等高。

网格行的相对高度。

- 如果 `start_cell='top-left'`，则按照从上到下赋值。
- 如果 `start_cell='bottom-left'`，则按照从下到上赋值。

### `specs=None`

二维 dict 列表或 `None`。

用于设置子图的类型、row/column spanning 以及间距等。

例如

- ex1: `specs=[[{}, {}], [{‘colspan’: 2}, None]]`
- ex2: `specs=[[{‘rowspan’: 2}, {}], [None, {}]]`

说明：

- 如果 `start_cell='top-left'`，外层列表的索引从顶部开始的网格行索引，如果 `start_cell='bottom-left'`，则为从底部开始的行索引。`specs` 中的行数必须和 `rows` 相等。
- 内部 list 的索引对应从左开始的列索引。`specs` 的列数必须和 `cols` 相等。
- `specs` 中的每一项对应网格中的一个 subplot
- 对空的 subplot，使用 `None` 代替
- `specs[0][0]` 对应 `start_cell` 中的subplot
- `specs` 的每一项都是一个字典

`specs` 字典可用 keys:

- `type`，subplot 类型，默认 'xy'，可选项
  - 'xy', 2D 笛卡尔子图类型
  - 'scene', 3D 笛卡尔子图类型
  - 'polar', 极坐标子图
  - 'ternary', scatterternary 的三元子图
  - 'mapbox', scattermapbox 的 Mapbox
  - 'domain', 单独定位的子图类型，如 pie, parcoords, parcats 等
  - trace type，根据 trace 类型名称，如 "bar", "scattergeo", "mesh" 等选择合适的 subplot 类型。
- `secondary_y`, bool, default False，如果为 True，在子图的右边添加一个 y 轴，只对 `type='xy'` 有效。
- `colspan`, int, default 1，子图占据的列数。
- `rowspan`, int, default 1，子图占据的行数。
- l, float, default 0.0，左边 padding（内边距）
- r, float, default 0.0, 右边 padding
- t, float, default 0.0, 上边 padding
- b, float, default 0.0, 下边 padding

### `insets=None`

list of dict or None。

Insets 是覆盖网格子图的子图。`insets` 用于指定 Insets。

`insets` 的每一项都是 dict。可用的 key 有：

- cell, tuple, default (1,1), 放置 inset 的(row, col) 索引
- type, string, default 'xy', 子图类型
- l, float, default=0.0, 左侧内边距（padding），以 cell 宽度比例值
- w, float 或 'to_end', default='to_end'，inset 宽度，以 cell width 比例计算，'to_end' 表示到 cell 右边
- b, float, default=0.0，底部内边距，cell 高度比例值
- h, float 或 'to_end', default='to_end'，inset 高度，cell 高度比例值

### `column_titles=None`

list of str or None.

在顶层放置的 columns 标题。

### `row_titles=None`

list of str or None.

最右放置的 rows 标题。

如果 `start_cell='top-left'`，标题从上到下放置。
否则从下到上放置。

### `x_title=None`

x 标题，放在最下面 row 的下面，水平居中。

### `y_title=None`

y 标题，放在最左 column 的左侧，垂直居中。

### `**kwargs`
