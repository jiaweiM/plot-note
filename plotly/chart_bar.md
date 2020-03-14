# Bar chart

- [Bar chart](#bar-chart)
  - [简介](#%e7%ae%80%e4%bb%8b)
    - [`data[type=bar]` 参数](#datatypebar-%e5%8f%82%e6%95%b0)
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
  - [Express API](#express-api)
    - [PX 垂直 Bar Chart](#px-%e5%9e%82%e7%9b%b4-bar-chart)
    - [PX 水平 Bar Chart](#px-%e6%b0%b4%e5%b9%b3-bar-chart)
    - [个性化](#%e4%b8%aa%e6%80%a7%e5%8c%96)
    - [Facetted subplots](#facetted-subplots)
    - [配置水平 bar chart](#%e9%85%8d%e7%bd%ae%e6%b0%b4%e5%b9%b3-bar-chart)
  - [plotly.graph_objects API](#plotlygraphobjects-api)
    - [GO 垂直 Bar Chart](#go-%e5%9e%82%e7%9b%b4-bar-chart)
    - [GO 水平 Bar Chart](#go-%e6%b0%b4%e5%b9%b3-bar-chart)
    - [Grouped Bar Chart](#grouped-bar-chart)
    - [GO Stacked Bar Chart](#go-stacked-bar-chart)
      - [垂直 Stacked Bar Chart](#%e5%9e%82%e7%9b%b4-stacked-bar-chart)
      - [水平 Stacked Bar Chart](#%e6%b0%b4%e5%b9%b3-stacked-bar-chart)
  - [Bar Chart with Hover Text](#bar-chart-with-hover-text)
  - [Bar Chart with Direct Labels](#bar-chart-with-direct-labels)
  - [uniformtext](#uniformtext)
  - [旋转坐标轴标签](#%e6%97%8b%e8%bd%ac%e5%9d%90%e6%a0%87%e8%bd%b4%e6%a0%87%e7%ad%be)
  - [设置单个 Bar 颜色](#%e8%ae%be%e7%bd%ae%e5%8d%95%e4%b8%aa-bar-%e9%a2%9c%e8%89%b2)
  - [设置单个 bar 宽度](#%e8%ae%be%e7%bd%ae%e5%8d%95%e4%b8%aa-bar-%e5%ae%bd%e5%ba%a6)
  - [设置初始值](#%e8%ae%be%e7%bd%ae%e5%88%9d%e5%a7%8b%e5%80%bc)
  - [颜色样式](#%e9%a2%9c%e8%89%b2%e6%a0%b7%e5%bc%8f)
  - [Relative Barmode](#relative-barmode)
  - [排序](#%e6%8e%92%e5%ba%8f)

## 简介

Plotly 中条形图用 [`plotly.graph_objects.Bar`](https://plot.ly/python/reference/#bar) 表示。

### `data[type=bar]` 参数

1. `orientation`
    - 'v' 垂直条形图，默认值
    - 'h' 水平条形图
2. `name`

trace 名称。在legend 以及鼠标在数据上悬停时显示。

3. `visible`
   - True，绘制 trace
   - False，不绘制 trace
   - "legendonly"，不绘制 trace，但 legend 可见

yongyu shehzi  trace 是否可见。

4. `showlegend`
    - default `True`

该 trace 的 legend 是否可见。

5. `x`

list, numpy array 或 Pandas series of numbers, strings or datetimes.

设置 x 坐标。

### marker

包含下面列出的一个或多个键值的字典。

#### line

parent: `data[type=bar].marker`

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

## Express API

### PX 垂直 Bar Chart

使用 `px.bar` 方法，`DataFrame` 的每一行用一个矩形表示。例如：

```py
import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop')
fig.show()
```

![bar](images/2020-03-12-17-27-05.png)

### PX 水平 Bar Chart

设置 `orientation='h'`

```py
import plotly.express as px
df = px.data.tips()
fig = px.bar(df, x="total_bill", y="day", orientation='h')
fig.show()
```

![horizontal](images/2020-03-14-09-42-47.png)

> 这里 x,y 位置不变

### 个性化

使用**关键字参数**个性化条形图。

例如：

```py
import plotly.express as px
data = px.data.gapminder()

data_canada = data[data.country == 'Canada']
fig = px.bar(data_canada, x='year', y='pop',
             hover_data=['lifeExp', 'gdpPercap'], color='lifeExp',
             labels={'pop':'population of Canada'}, height=400)
fig.show()
```

![custom bar](images/2020-03-13-21-08-32.png)

- 当多行使用相同的 `x` 值，矩形默认互相叠加：

```py
import plotly.express as px
df = px.data.tips()
fig = px.bar(df, x="sex", y="total_bill", color='time')
fig.show()
```

![multiple](images/2020-03-13-21-10-40.png)

- 通过 `barmode` 修改默认堆叠行为

```py
fig = px.bar(df, x="sex", y="total_bill", color='smoker', barmode='group',
             height=400)
fig.show()
```

![group](images/2020-03-13-21-16-29.png)

### Facetted subplots

使用关键字参数 `facet_row` (或 `facet_col`) 创建子图，dataframe 中和 `facet_row` 对应的每个不同值创建不同的子图。例如：

```py
import plotly.express as px
fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group",
             facet_row="time", facet_col="day",
             category_orders={"day": ["Thur", "Fri", "Sat", "Sun"],
                              "time": ["Lunch", "Dinner"]})
fig.show()
```

![facet](images/2020-03-13-21-22-13.png)

`facet_row` 指定的 "time" 有两个值，所以图分为了上下两行。

`facet_col` 指定的 "day" 包含四个值，所有图分为了四列。

### 配置水平 bar chart

- 设置颜色和hover data

```py
import plotly.express as px
df = px.data.tips()
fig = px.bar(df, x="total_bill", y="sex", color='day', orientation='h',
             hover_data=["tip", "size"],
             height=400,
             title='Restaurant bills')
fig.show()
```

![colored](images/2020-03-14-09-47-45.png)

## plotly.graph_objects API

`plotly.graph_objects` 中的 `go.Bar` 函数更为通用，[API 参考](https://plot.ly/python/reference/#bar)。

### GO 垂直 Bar Chart

```py
import plotly.graph_objects as go
animals=['giraffes', 'orangutans', 'monkeys']

fig = go.Figure([go.Bar(x=animals, y=[20, 14, 23])])
fig.show()
```

![bar](images/2020-03-13-21-28-04.png)

### GO 水平 Bar Chart

```py
import plotly.graph_objects as go

fig = go.Figure(go.Bar(
            x=[20, 14, 23],
            y=['giraffes', 'orangutans', 'monkeys'],
            orientation='h'))

fig.show()
```

![bar](images/2020-03-14-09-52-05.png)

### Grouped Bar Chart

使用 `fig.update` 自定义 figure。

```py
import plotly.graph_objects as go

animals = ['giraffes', 'orangutans', 'monkeys']

fig = go.Figure(data=[
    go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),
    go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()
```

![group bar](images/2020-03-13-21-32-53.png)

### GO Stacked Bar Chart

#### 垂直 Stacked Bar Chart

```py
import plotly.graph_objects as go

animals = ['giraffes', 'orangutans', 'monkeys']

fig = go.Figure(data=[
    go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),
    go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])
])
# Change the bar mode
fig.update_layout(barmode='stack')
fig.show()
```

![stacked barchart](images/2020-03-13-21-34-51.png)

#### 水平 Stacked Bar Chart



## Bar Chart with Hover Text

即将鼠标放在图上弹出来的提示文字。

```py
import plotly.graph_objects as go

x = ['Product A', 'Product B', 'Product C']
y = [20, 14, 23]

# Use the hovertext kw argument for hover text
fig = go.Figure(data=[go.Bar(x=x, y=y,
                             hovertext=['27% market share', '24% market share', '19% market share'])])
# custoize aspect
fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
fig.update_layout(title_text='January 2013 Sales Report')
fig.show()
```

![hover text](images/2020-03-13-21-41-49.png)

## Bar Chart with Direct Labels

即在条形图上显示标签。

- 通过关键字参数 `text` 设置标签值
- 通过 `textposition` 设置标签位置

```py
import plotly.graph_objects as go

x = ['Product A', 'Product B', 'Product C']
y = [20, 14, 23]

# Use textposition='auto' for direct text
fig = go.Figure(data=[go.Bar(x=x, y=y,
                             text=y, textposition='auto')])
fig.show()
```

![label](images/2020-03-13-21-44-55.png)

## uniformtext

通过 layout 的 `uniformtext` 参数可以设置所有的文本标签字体大小相同。

- `minsize` 属性设置字体大小
- `mode` 属性设置当空间不足以以指定 fontsize 显示标签时的行为：
  - 'hide' 隐藏标签
  - 'show' 显示标签
- `textposition`，设置标签位置

```py
import plotly.express as px

df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
fig = px.bar(df, y='pop', x='country', text='pop')
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.show()
```

![label](images/2020-03-13-21-50-42.png)

## 旋转坐标轴标签

```py
import plotly.graph_objects as go

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

fig = go.Figure()
fig.add_trace(go.Bar(
    x=months,
    y=[20, 14, 25, 16, 18, 22, 19, 15, 12, 16, 14, 17],
    name='Primary Product',
    marker_color='indianred'
))
fig.add_trace(go.Bar(
    x=months,
    y=[19, 14, 22, 14, 16, 19, 15, 14, 10, 12, 12, 16],
    name='Secondary Product',
    marker_color='lightsalmon'
))

# Here we modify the tickangle of the xaxis, resulting in rotated labels.
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()
```

![rotated label](images/2020-03-13-21-52-43.png)

## 设置单个 Bar 颜色

```py
import plotly.graph_objects as go

colors = ['lightslategray',] * 5
colors[1] = 'crimson'

fig = go.Figure(data=[go.Bar(
    x=['Feature A', 'Feature B', 'Feature C',
       'Feature D', 'Feature E'],
    y=[20, 14, 23, 25, 22],
    marker_color=colors # marker color can be a single color value or an iterable
)])
fig.update_layout(title_text='Least Used Feature')
```

![bar color](images/2020-03-13-21-54-15.png)

## 设置单个 bar 宽度

```py
import plotly.graph_objects as go

fig = go.Figure(data=[go.Bar(
    x=[1, 2, 3, 5.5, 10],
    y=[10, 8, 6, 4, 2],
    width=[0.8, 0.8, 0.8, 3.5, 4] # customize width here
)])

fig.show()
```

![width](images/2020-03-13-21-55-12.png)

## 设置初始值

bar 的 y 值为在初始值（base）上增加的值。

```py
import plotly.graph_objects as go

years = ['2016','2017','2018']

fig = go.Figure()
fig.add_trace(go.Bar(x=years, y=[500, 600, 700],
                base=[-500,-600,-700],
                marker_color='crimson',
                name='expenses'))
fig.add_trace(go.Bar(x=years, y=[300, 400, 700],
                base=0,
                marker_color='lightslategrey',
                name='revenue'
                ))

fig.show()
```

![base](images/2020-03-13-21-57-33.png)

## 颜色样式

下面自定义参数较多，因此使用 `go.Layout()` 比使用 `fig.update` 更方便。

```py
import plotly.graph_objects as go

years = [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
         2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012]

fig = go.Figure()
fig.add_trace(go.Bar(x=years,
                y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                   350, 430, 474, 526, 488, 537, 500, 439],
                name='Rest of world',
                marker_color='rgb(55, 83, 109)'
                ))
fig.add_trace(go.Bar(x=years,
                y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                   299, 340, 403, 549, 499],
                name='China',
                marker_color='rgb(26, 118, 255)'
                ))

fig.update_layout(
    title='US Export of Plastic Scrap',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='USD (millions)',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig.show()
```

![colored barchart](images/2020-03-13-22-02-07.png)

## Relative Barmode

在 "relative" 模式下，不同 bars 互相堆叠。正值在坐标轴上，负值在坐标轴下。

```py
import plotly.graph_objects as go
x = [1, 2, 3, 4]

fig = go.Figure()
fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16]))
fig.add_trace(go.Bar(x=x, y=[6, -8, -4.5, 8]))
fig.add_trace(go.Bar(x=x, y=[-15, -3, 4.5, -8]))
fig.add_trace(go.Bar(x=x, y=[-1, 3, -3, -4]))

fig.update_layout(barmode='relative', title_text='Relative Barmode')
fig.show()
```

![relative barmode](images/2020-03-13-22-05-55.png)

## 排序

排序设置 `categoryorder`：

- 对字符串，设置为 "category ascending" 或 "category descending"
- 对数值，设置 "total ascending" 或 "total descending"

注意，目前无法按照特定的 trace 进行排序，而只能按照总和进行排序。如果需要更多排序，可以对数据排序好再进行绘图。

实例：

```py
import plotly.graph_objects as go

x=['b', 'a', 'c', 'd']
fig = go.Figure(go.Bar(x=x, y=[2,5,1,9], name='Montreal'))
fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16], name='Ottawa'))
fig.add_trace(go.Bar(x=x, y=[6, 8, 4.5, 8], name='Toronto'))

fig.update_layout(barmode='stack', xaxis={'categoryorder':'category ascending'})
fig.show()
```

![categoryorder](images/2020-03-13-22-11-43.png)

- 通过指定 `categoryarray` 指定顺序

```py
import plotly.graph_objects as go

x=['b', 'a', 'c', 'd']
fig = go.Figure(go.Bar(x=x, y=[2,5,1,9], name='Montreal'))
fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16], name='Ottawa'))
fig.add_trace(go.Bar(x=x, y=[6, 8, 4.5, 8], name='Toronto'))

fig.update_layout(barmode='stack', xaxis={'categoryorder':'array', 'categoryarray':['d','a','c','b']})
fig.show()
```

![categoryarray](images/2020-03-13-22-12-50.png)

- 总值降序

设置 `categoryorder: 'total descending'`

```py
import plotly.graph_objects as go

x=['b', 'a', 'c', 'd']
fig = go.Figure(go.Bar(x=x, y=[2,5,1,9], name='Montreal'))
fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16], name='Ottawa'))
fig.add_trace(go.Bar(x=x, y=[6, 8, 4.5, 8], name='Toronto'))

fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
fig.show()
```

![descending](images/2020-03-14-09-39-40.png)