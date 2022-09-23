# matplotlib.pyplot.axis

Last updated: 2022-09-23, 11:08
****

## 概述

```python
matplotlib.pyplot.axis(*args, emit=True, **kwargs)
```

查询或设置坐标轴属性的便捷方法。

调用方法签名：

```python
xmin, xmax, ymin, ymax = axis()
xmin, xmax, ymin, ymax = axis([xmin, xmax, ymin, ymax])
xmin, xmax, ymin, ymax = axis(option)
xmin, xmax, ymin, ymax = axis(**kwargs)
```

## 参数

**xmin, xmax, ymin, ymax: float, optional**

设置坐标轴范围，也可以采用如下方式：

```python
ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))
```

**option: bool or str**

如果是 bool 值，表示打开或关闭坐标轴线和标签。如果是字符串，选项有：

|值|说明|
|---|---|
|'on'|启用轴线和标签，等价于 `True`|
|'off'|关闭轴线和标签，等价于 `False`|
|'equal'|通过设置轴 limits 设置相等缩放（使圆成为圆）。等价于 `ax.set_aspect('equal', adjustable='datalim')`。可能不尊重数据范围|
|'scaled'|通过设置绘图框的尺寸来设置相等缩放（使圆成为圆）。等价于 `ax.set_aspect('equal', adjustable='box', anchor='C')`。此外，将禁用进一步的自动缩放|
|'tight'|设置 limits 刚好足够显示所有数据，禁用进一步的自动缩放|
|'auto'|自动缩放|
|'image'|缩放到坐标轴 limit 等于 数据 Limit|
|'square'|方块图，类似 `'scaled'`，但是强制 `xmax-xmin == ymax-ymin`|

**emit: bool, default: True**

是否通知 observers 坐标轴 limit 的更改。该选项被传递给 `set_xlim` 和 `set_ylim`。

## 返回

**xmin, xmax, ymin, ymax: float**

坐标轴范围。

## 参考

- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html
