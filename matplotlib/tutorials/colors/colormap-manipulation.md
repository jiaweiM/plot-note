# 创建 Colormap

## 简介

`matplotlib.colormaps` 中内置有许多 colormaps。也有一些外部库，如 [Palettable](https://jiffyclub.github.io/palettable/) 提供了许多额外的 colormaps。

另外还可以使用 `ListedColormap` 或 `LinearSegmentedColormap` 自定义 colormap。这两个 colormap 类都将 0 到 1 之间的值映射到一组颜色。

在手动创建 colormap 前，先介绍如何获得现有 colormap 以及它们的颜色。

## 获取 colormap

colormap 中定义的颜色列表可以通过 `Colormap.resampled` 调整。

## 参考

- https://matplotlib.org/stable/tutorials/colors/colormap-manipulation.html
