# matplotlib.pyplot.plot

***

```python
matplotlib.pyplot.plot(*args, scalex=True, scaley=True, data=None, **kwargs)
```

y 对 x 绘制直线或 marker。

调用签名：

```python
plot([x], y, [fmt], *, data=None, **kwargs)
plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)
```

参数 `fmt` 用来定义基本格式，如颜色、标记和线条样式。例如：

```python
plot(x, y)        # 使用默认线条样式和颜色绘制 x 和 y
plot(x, y, 'bo')  # 使用蓝色圆圈绘制 x 和 y
plot(y)           # x 为默认索引值 0..N-1
plot(y, 'r+')     # 同上，但带有红色加号
```
