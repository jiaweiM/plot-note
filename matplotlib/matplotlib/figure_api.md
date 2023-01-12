# matplotlib.figure

- [matplotlib.figure](#matplotlibfigure)
  - [简介](#简介)
  - [Figure](#figure)
    - [subplots\_adjust](#subplots_adjust)
  - [FigureBase](#figurebase)
  - [SubFigure](#subfigure)
  - [SubplotParams](#subplotparams)
  - [figaspect()](#figaspect)
  - [参考](#参考)

***

## 简介

`matplotlib.figure` 实现了如下类：

- [Figure](#figure)

顶层 `Artist`，包含所有 plot 元素。许多方法在 [FigureBase](#figurebase) 中实现。

- [SubFigure](#subfigure)

figure 中的逻辑 figure，通常使用 `Figure.add_subfigure` 或 `Figure.subfigures` 方法添加到 figure。

- [SubplotParams](#subplotparams)

设置 subplots 之间的默认间距。

## Figure

```python
class matplotlib.figure.Figure(
    figsize=None, 
    dpi=None, 
    *, 
    facecolor=None, 
    edgecolor=None, 
    linewidth=0.0, 
    frameon=None, 
    subplotpars=None, 
    tight_layout=None, 
    constrained_layout=None, 
    layout=None, 
    **kwargs)
```

### subplots_adjust

```python
subplots_adjust(
    left=None, bottom=None, right=None, top=None, 
    wspace=None, hspace=None)
```

调整 subplot 布局参数。

未设置的参数保持不变，初始值为 `rcParams["figure.subplot.[name]"]`。

**参数：**

- **left** 和 **right**: `float`, optional

subplots 左侧和右侧边缘位置，定义为 figure width 的比例。

- **bottom** 和 **top**: `float`, optional

subplots 底部和顶部边缘位置，定义为 figure height 的比例。

- **wspace** 和 **hspace**: `float`, optional

subplots 之间填充的宽度和高度，定义为 Axes 平均宽度或高度的比例。

## FigureBase

## SubFigure

## SubplotParams

## figaspect()

## 参考

- https://matplotlib.org/stable/api/figure_api.html
