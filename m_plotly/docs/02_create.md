- [图表达方式](#%e5%9b%be%e8%a1%a8%e8%be%be%e6%96%b9%e5%bc%8f)
  - [字典](#%e5%ad%97%e5%85%b8)
  - [图形对象方式](#%e5%9b%be%e5%bd%a2%e5%af%b9%e8%b1%a1%e6%96%b9%e5%bc%8f)
- [创建图形](#%e5%88%9b%e5%bb%ba%e5%9b%be%e5%bd%a2)
  - [构造函数](#%e6%9e%84%e9%80%a0%e5%87%bd%e6%95%b0)
  - [Plotly express](#plotly-express)
  - [Figure factories](#figure-factories)
  - [生成子图](#%e7%94%9f%e6%88%90%e5%ad%90%e5%9b%be)
- [更新图](#%e6%9b%b4%e6%96%b0%e5%9b%be)
  - [添加图（Adding trace）](#%e6%b7%bb%e5%8a%a0%e5%9b%beadding-trace)
  - [添加 trace 到 subplots](#%e6%b7%bb%e5%8a%a0-trace-%e5%88%b0-subplots)
  - [Add trace 的简易方法](#add-trace-%e7%9a%84%e7%ae%80%e6%98%93%e6%96%b9%e6%b3%95)
  - [下划线](#%e4%b8%8b%e5%88%92%e7%ba%bf)
  - [update layout 方法](#update-layout-%e6%96%b9%e6%b3%95)
  - [update trace 方法](#update-trace-%e6%96%b9%e6%b3%95)
  - [参数覆盖](#%e5%8f%82%e6%95%b0%e8%a6%86%e7%9b%96)
# 图表达方式
## 字典
plotly.py 的主要目的是提供 plotly.js JavaScript 库的接口。在 Plotly.js 中，图形是由声明式的 JSON 数据结构指定。plotly.py 需要提供 Python 字典形式的数据，以方便序列化为 JSON 数据结构。

下面是一个包含一个条形图数据和标题的字典：
```py
fig = {
    "data": [{"type": "bar",
              "x": [1, 2, 3],
              "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Bar Chart"}}
}

# To display the figure defined by this dict, use the low-level plotly.io.show function
import plotly.io as pio
pio.show(fig)
```

可以发现，整个字典都是按照类似于 JSON 的数据结构进行组织。效果：

![](images/plot1.png)

顶层 "data" 包含数据值的列表：
- `type` 指定图类型；
- 余下用于指定图的各种配置

"layout" 用于指定图的布局。

## 图形对象方式
除了 Python 字典，plotly.py 还提供了一种创建方式，即通过一系列的图形对象创建图标。相对字典，使用图形类具有如下优点：
- Graph 对象提供了数据验证功能。所以如果提供了无效的属性名称或值，可以看到有用的错误信息。
- Graph 对象的 Python 文档包含对每个属性的说明。可以参看这些文档而不是专门去 plotly 官网查询参考。
- Graph 对象属性可以通过键查找（如 `fig["layout"]`），或者访问对象式的方式（`fig.layout`）。
- Graph 对象支持更新已创建的图更方便。

Graph 对象以属性结构保存在 `plotly.graph_objects` 包中。下面用对象方式创建和上面相同的图：
```py
import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
    layout=go.Layout(
        title=go.layout.Title(text="A Bar Chart")
    )
)

fig.show()
```

还可以采用混合模式：
```py
import plotly.graph_objects as go
fig = go.Figure({
    "data": [{"type": "bar",
              "x": [1, 2, 3],
              "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Bar Chart"}}
})
fig.show()
```

创建好图形对象后，可以通过 `fig.to_dict()` 将图形转换为字典，使用 `fig.to_json()` 将图形转换为 JSON。

# 创建图形
下面总结创建图形的方式。

## 构造函数
如前面所示，可以将图形所需的完整数据传递给 `plotly.graph_objects.Figure` 构造函数创建图形。
```py
import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
    layout=dict(title=dict(text="A Bar Chart"))
)
fig.show()
```

## Plotly express
Plotly express 是生成图形对象的高级API。例如：
```py
import plotly.express as px
iris = px.data.iris()
fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species")

# If you print fig, you'll see that it's just a regular figure with data and layout
# print(fig)

fig.show()
```

![](images/plot2.png)

## Figure factories
Figure factories 是用于生成图形对象的的方法。例如：
```py
import numpy as np
import plotly.figure_factory as ff
x1,y1 = np.meshgrid(np.arange(0, 2, .2), np.arange(0, 2, .2))
u1 = np.cos(x1)*y1
v1 = np.sin(x1)*y1

fig = ff.create_quiver(x1, y1, u1, v1)
fig.show()
```

![](images/plot3.png)

## 生成子图
`plotly.subplots.make_subplots` 函数可以生成包含多个子图的图形。例：
```py
from plotly.subplots import make_subplots
fig = make_subplots(rows=1, cols=2)
fig.add_trace(go.Scatter(y=[4, 2, 1], mode="lines"), row=1, col=1)
fig.add_trace(go.Bar(y=[2, 1, 3]), row=1, col=2)
fig.show()
```

![](images/plot4.png)

# 更新图
不管图形以什么方式创建，都可以继续添加图形或修改属性。

> 对一个图，plotly 将其称为 trace.

## 添加图（Adding trace）
可以使用 `add_trace` 方法添加新图。该方法接受graph 对象参数。例如，下面先创建一个空的 figure，然后添加一个图：
```py
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
fig.show()
```

或者使用 figure 工厂或 plotly express 创建的图：
```py
iris = px.data.iris()
fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species")
fig.add_trace(
    go.Scatter(
        x=[2, 4],
        y=[4, 8],
        mode="lines",
        line=go.scatter.Line(color="gray"),
        showlegend=False)
)
fig.show()
```

![](images/plot5.png)

## 添加 trace 到 subplots
如果 figure 是使用 `plotly.subplots.make_subplots` 创建，则调用 `add_trace` 时可以指定 `row` 和 `col` 参数。

```py
from plotly.subplots import make_subplots
fig = make_subplots(rows=1, cols=2)
fig.add_trace(go.Scatter(y=[4, 2, 1], mode="lines"), row=1, col=1)
fig.add_trace(go.Bar(y=[2, 1, 3]), row=1, col=2)
fig.show()
```

![](images/plot6.png)

对 plotly express，如果使用了 `facet_row` 或 `facet_col` 参数，也具有该功能：
```py
import plotly.express as px
iris = px.data.iris()
fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species", facet_col="species")
reference_line = go.Scatter(x=[2, 4],
                            y=[4, 8],
                            mode="lines",
                            line=go.scatter.Line(color="gray"),
                            showlegend=False)
fig.add_trace(reference_line, row=1, col=1)
fig.add_trace(reference_line, row=1, col=2)
fig.add_trace(reference_line, row=1, col=3)
fig.show()
```

## Add trace 的简易方法
除了 `add_trace` 方法，graph figure 对象包含一系列的 `add_{trace}`方法，如 `add_scatter`, `add_var` 等。

```py
from plotly.subplots import make_subplots
fig = make_subplots(rows=1, cols=2)
fig.add_scatter(y=[4, 2, 1], mode="lines", row=1, col=1)
fig.add_bar(y=[2, 1, 3], row=1, col=2)
fig.show()
```

## 下划线
为了能够更容易访问属性，Plotly 支持通过下划线连接访问属性。

例如，如果不使用下划线，设置标题需要将 `layout` 属性设置为 `dict(title=dict(text="A Chart"))`，类似的，设置 scatter trace 的线条颜色需要设置 `marker` 属性为 `dict(color="crimson")`。

如下：
```py
import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Scatter(y=[1, 3, 2], line=dict(color="crimson"))],
    layout=dict(title=dict(text="A Chart"))
)
fig.show()
```

而使用下划线要简单许多：
```py
import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Scatter(y=[1, 3, 2], line_color="crimson")],
    layout_title_text="A Chart"
)
fig.show()
```

## update layout 方法
Graph figure 对象提供的 `update_layout` 方法可用于一次更新 layout 的多个属性。例如：
```py
import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
fig.update_layout(title_text="A Bar Chart",
                  title_font_size=30)
fig.show()
```

如下的这些操作是等效的：
```py
fig.update_layout(title_text="A Bar Chart",
                  title_font_size=30)

fig.update_layout(title_text="A Bar Chart",
                  title_font=dict(size=30))


fig.update_layout(title=dict(text="A Bar Chart"),
                             font=dict(size=30))

fig.update_layout({"title": {"text": "A Bar Chart",
                             "font": {"size": 30}}})

fig.update_layout(
    title=go.layout.Title(text="A Bar Chart",
                          font=go.layout.title.Font(size=30)));
```

## update trace 方法
`update_traces` 方法可以更新 figure 中的多个 traces 的多个属性。

为了演示该方法，下面使用两个各自包含 bar 和 scatter traces 的两个 subplots 作为例子：
```py
from plotly.subplots import make_subplots
fig = make_subplots(rows=1, cols=2)

fig.add_scatter(y=[4, 2, 3.5], mode="markers",
                marker=dict(size=20, color="LightSeaGreen"),
                name="a", row=1, col=1)

fig.add_bar(y=[2, 1, 3],
            marker=dict(color="MediumPurple"),
            name="b", row=1, col=1)

fig.add_scatter(y=[2, 3.5, 4], mode="markers",
                marker=dict(size=20, color="MediumPurple"),
                name="c", row=1, col=2)

fig.add_bar(y=[1, 3, 2],
            marker=dict(color="LightSeaGreen"),
            name="d", row=1, col=2)

fig.show()
```

![](images/plot7.png)

`scatter` 和 `bar` traces 都有 `marker.color` 属性，下面使用 `update_traces` 修饰所有 traces 的颜色：
```py
from plotly.subplots import make_subplots
fig = make_subplots(rows=1, cols=2)

fig.add_scatter(y=[4, 2, 3.5], mode="markers",
                marker=dict(size=20, color="LightSeaGreen"),
                name="a", row=1, col=1)

fig.add_bar(y=[2, 1, 3],
            marker=dict(color="MediumPurple"),
            name="b", row=1, col=1)

fig.add_scatter(y=[2, 3.5, 4], mode="markers",
                marker=dict(size=20, color="MediumPurple"),
                name="c", row=1, col=2)

fig.add_bar(y=[1, 3, 2],
            marker=dict(color="LightSeaGreen"),
            name="d", row=1, col=2)

fig.update_traces(marker=dict(color="RoyalBlue"))

fig.show()
```

![](images/plot8.png)

`update_traces` 方法支持 `selector` 参数，用于选择需要更新的 traces。例如，只更新 `bar` 的颜色：
```py
from plotly.subplots import make_subplots
fig = make_subplots(rows=1, cols=2)

fig.add_scatter(y=[4, 2, 3.5], mode="markers",
                marker=dict(size=20, color="LightSeaGreen"),
                name="a", row=1, col=1)

fig.add_bar(y=[2, 1, 3],
            marker=dict(color="MediumPurple"),
            name="b", row=1, col=1)

fig.add_scatter(y=[2, 3.5, 4], mode="markers",
                marker=dict(size=20, color="MediumPurple"),
                name="c", row=1, col=2)

fig.add_bar(y=[1, 3, 2],
            marker=dict(color="LightSeaGreen"),
            name="d", row=1, col=2)

fig.update_traces(marker=dict(color="RoyalBlue"),
                  selector=dict(type="bar"))

fig.show()
```

![](images/plot9.png)

在 selector 中可以使用下划线。例如，值更新颜色为 "MediumPurple" 的颜色：
```py
from plotly.subplots import make_subplots
fig = make_subplots(rows=1, cols=2)

fig.add_scatter(y=[4, 2, 3.5], mode="markers",
                marker=dict(size=20, color="LightSeaGreen"),
                name="a", row=1, col=1)

fig.add_bar(y=[2, 1, 3],
            marker=dict(color="MediumPurple"),
            name="b", row=1, col=1)

fig.add_scatter(y=[2, 3.5, 4], mode="markers",
                marker=dict(size=20, color="MediumPurple"),
                name="c", row=1, col=2)

fig.add_bar(y=[1, 3, 2],
            marker=dict(color="LightSeaGreen"),
            name="d", row=1, col=2)

fig.update_traces(marker_color="RoyalBlue",
                  selector=dict(marker_color="MediumPurple"))

fig.show()
```

![](images/plot10.png)

对包含 subplots 的 figure，`update_traces` 方法也支持 `row`, `col` 参数，用于控制被更新的 trace。例如，下面只更新第二列的 traces:
```py
from plotly.subplots import make_subplots
fig = make_subplots(rows=1, cols=2)

fig.add_scatter(y=[4, 2, 3.5], mode="markers",
                marker=dict(size=20, color="LightSeaGreen"),
                name="a", row=1, col=1)

fig.add_bar(y=[2, 1, 3],
            marker=dict(color="MediumPurple"),
            name="b", row=1, col=1)

fig.add_scatter(y=[2, 3.5, 4], mode="markers",
                marker=dict(size=20, color="MediumPurple"),
                name="c", row=1, col=2)

fig.add_bar(y=[1, 3, 2],
            marker=dict(color="LightSeaGreen"),
            name="d", row=1, col=2)

fig.update_traces(marker=dict(color="RoyalBlue"),
                  col=2)

fig.show()
```

![](images/plot11.png)

## 参数覆盖
`update_layout` 和 `update_traces` 有一个 `overwrite` 关键字参数，默认为 `False`，