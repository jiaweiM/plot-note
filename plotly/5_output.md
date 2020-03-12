# Output Image

- [Output Image](#output-image)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [安装依赖项](#%e5%ae%89%e8%a3%85%e4%be%9d%e8%b5%96%e9%a1%b9)
  - [创建图](#%e5%88%9b%e5%bb%ba%e5%9b%be)
  - [输出图像文件](#%e8%be%93%e5%87%ba%e5%9b%be%e5%83%8f%e6%96%87%e4%bb%b6)
    - [Raster Formats: PNG, JPEG, and WebP](#raster-formats-png-jpeg-and-webp)
    - [Vector Formats: SVG and PDF](#vector-formats-svg-and-pdf)
- [获得图像字节](#%e8%8e%b7%e5%be%97%e5%9b%be%e5%83%8f%e5%ad%97%e8%8a%82)
- [使用 `IPython.display.Image` 显式 Bytes 图像](#%e4%bd%bf%e7%94%a8-ipythondisplayimage-%e6%98%be%e5%bc%8f-bytes-%e5%9b%be%e5%83%8f)
  
## 简介

Plotly 可以将 figure 保存为静态图像。

在浏览器中显示的 Ploly figures 可以交互，也可以导出为 PNG, JPEG, SVG或PDF。

## 安装依赖项

图片生成功能需要 orca 命令行工具以及 `psutil`, `requests` Python 库。

orca 安装参考[简介](1_intro.md)

## 创建图

```py
import plotly.graph_objects as go
import numpy as np
np.random.seed(1)

N = 100
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sz = np.random.rand(N) * 30

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode="markers",
    marker=go.scatter.Marker(
        size=sz,
        color=colors,
        opacity=0.6,
        colorscale="Viridis"
    )
))

fig.show()
```

## 输出图像文件

`plotly.io.write_image` 函数用于输出图像文件。也可以使用图形对象的 `.write_image` 方法。

首先，创建保存图像的目录：

```py
if not os.path.exists("images"):
    os.mkdir("images")
```

### Raster Formats: PNG, JPEG, and WebP

PNG：

```py
fig.write_image("images/fig1.png")
```

JPEG:

```py
fig.write_image("images/fig1.jpeg")
```

WebP:

```py
fig.write_image("images/fig1.webp")
```

### Vector Formats: SVG and PDF

SVG:

```py
fig.write_image("images/fig1.svg")
```

PDF:

```py
fig.write_image("images/fig1.pdf")
```

EPS（需要 `poppler` 库）

```py
fig.write_image("images/fig1.eps")
```

> NOTE：对包含 WebGL 轨迹的图形（如 scattergl, heatmapgl, contourgl, scatter3d, surface, mesh3d, scatterpolargl, cone, streamtube, splom, parcoords）导出为矢量图格式时，图像的部分区域会以栅格的形式封装，而不是矢量。

# 获得图像字节
`plotly.io.to_image` 将图像转换为字节。

例如将 PNG 转换为字节：
```py
img_bytes = fig.to_image(format="png")
```

然后输出前 20 个字节：
```
img_bytes[:20]
```

# 使用 `IPython.display.Image` 显式 Bytes 图像
```py
from IPython.display import Image
Image(img_bytes)
```