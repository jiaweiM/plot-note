# matplotlib.pyplot.axis

***

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
|'equal'|

Set equal scaling (i.e., make circles circular) by changing axis limits. This is the same as ax.set_aspect('equal', adjustable='datalim'). Explicit data limits may not be respected in this case.

'scaled'

Set equal scaling (i.e., make circles circular) by changing dimensions of the plot box. This is the same as ax.set_aspect('equal', adjustable='box', anchor='C'). Additionally, further autoscaling will be disabled.

'tight'

Set limits just large enough to show all data, then disable further autoscaling.

'auto'

Automatic scaling (fill plot box with data).

'image'

'scaled' with axis limits equal to data limits.

'square'

Square plot; similar to 'scaled', but initially forcing xmax-xmin == ymax-ymin.