# Introduction

- [Introduction](#introduction)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [安装](#%e5%ae%89%e8%a3%85)
  - [Jupyter Notebook 支持](#jupyter-notebook-%e6%94%af%e6%8c%81)
  - [静态图像导出](#%e9%9d%99%e6%80%81%e5%9b%be%e5%83%8f%e5%af%bc%e5%87%ba)

## 简介

plotly Python 库（plotly.py）是一个交互式的开源绘图库，它支持40多种图标类型，涵盖了统计、财务、地理和科学等方面。

plotly.py 构建在 plotly.js 上，使 Python 用户可以创建基于 web 的漂亮交互式可视化图。

## 安装

通过 pip 安装：

```cmd
pip install plotly==4.5.2
```

通过 conda 安装：

```cmd
conda install -c plotly plotly=4.5.2
```

该工具包包含将可视化图写入HTML的所有工具。

## Jupyter Notebook 支持

安装 jupyter 之后，直接运行：

```py
import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.show()
```

即可显示图形：

![bar](images/2020-03-11-16-44-39.png)

## 静态图像导出

使用 `plotly.io` 包中的 `to_image` 和 `write_image` 函数可以导出静态图像。

使用该功能需要安装 `orca` 命令行工具和 `psutil`, `requests` Python 包。

> `requests` 包用于 Python 进程与本地orca服务进程交互，不会和外部服务交互。

orca 下载地址：[https://github.com/plotly/orca/releases](https://github.com/plotly/orca/releases)
