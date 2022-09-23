# matplotlib.axes.Axes.set_xlim

Last updated: 2022-09-23, 10:55
****

## 概述

```python
Axes.set_xlim(left=None, right=None, *, emit=True, auto=False, xmin=None, xmax=None)
```

设置 x 轴范围。

## 参数

**left: float, optional**

数据坐标 left xlim。`None` 表示保持不变。left 和 right xlims 也可以作为 tuple `(left, right)` 以第一个参数传入。

**right: float, optional**

数据坐标 right xlim。`None` 表示保持不变。

**emit: bool, default: True**

是否向 observers 发送 limit 变化通知。

**auto: bool or None, default: False**

是否启用 x 轴的自动缩放。`True` 启用，`False` 关闭，`None` 维持不变。

**xmin, xmax: float, optional**

分别等价于 `left` 和 `right`，同时传入 `left` 和 `xmin` 或 `right` 和 `xmax` 会报错。

## 返回

**left, right: (float, float)**

数据坐标中 x 轴新的范围。

## 注意项

`left` 值可以大于 `right`，此时 x 轴的值从左向右减小。

## 示例

```python
set_xlim(left, right)
set_xlim((left, right))
left, right = set_xlim(left, right)
```

只设置一个，另一个范围不变：

```python
set_xlim(right=right_lim)
```

也可以按相反顺序传递 xlim，使 x 轴反向反转。例如，假设 x 表示多少年前。可以按如下方式设置坐标轴，此时 5000 表示 5000 年前，在坐标轴左侧，0 表示现在，在坐标轴右侧：

```python
set_xlim(5000, 0)
```

## 参考

- https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html
