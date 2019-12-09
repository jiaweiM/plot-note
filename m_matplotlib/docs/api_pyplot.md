# TOC
- [TOC](#toc)
- [pyplot.acorr](#pyplotacorr)
- [pyplot.figure](#pyplotfigure)
- [pyplot.hist](#pyplothist)

# pyplot.acorr
```py
matplotlib.pyplot.acorr(x, *, data=None, **kwargs)[source]
```
绘制 x 的自相关。

|参数|说明|
|---|---|
|x|array-like|

# pyplot.figure
```py
matplotlib.pyplot.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)[source]
```
创建一个新的 figure.

|参数|类型|说明|
|---|---|---|
|num|integer or string, optional, default, None|如果不提供，创建一个新的 figure，figure 编号增加。figure 的编号保存在 `number` 属性中。如果提供 `num`已有对应的 figure，激活该 figure 并返回其引用。如果不存在具有该编号的 figure，创建并返回具有该编号的 figure。如果 `num` 是 string 类型，窗口的标题被设置为 `num`|
|figsize|(float, float), optional, default `None`|figure 的宽度和高度，单位英寸，如果不提供值，默认为 `rcParams["figure.figsize"] = [6.4, 4.8]`|
|dpi|integer, optional, default `None`|figure 分辨率，默认为 `rcParams["figure.dpi" = 100.0]`|
|facecolor|color spec|背景色，默认为 `rcParams["figure.facecolor"] = 'white'` = 'w'|
|edgecolor|color spec|边框色，默认为 `rcParams["figure.edgecolor"] = 'white'` = 'w'|
|frameon|bool, optional, default: `True`|是否绘制 figure 的框|
|FigureClass|`Figure` 的子类, optional|使用自定义的 `Figure` 实例|
|clear|bool, optional, default `False`|如果为 True 并且对应的 figure 已存在，则清除该 figure|

额外的 kwargs 参数传递给 `Figure` 的初始化函数。

返回创建的 `Figure` 实例。

创建 `Figure` 实例同时会传递给后端的 *new_figure_manager*，从而将自定义的 Figure 类连接到 pyplot 接口。

> 如果创建了许多 figures，应该显式调用 `pyplot.close()` 以清除内存。


# pyplot.hist
```py
matplotlib.pyplot.hist(x, bins=None, range=None, density=None, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, normed=None, *, data=None, **kwargs)
```
绘制直方图。

计算并绘制 x 的直方图。返回 `(n, bins, patches)`，如果输入包含多个数据，则返回 `([n0, n1,...], bins, [patches0, patches1,...])`。

对多组数据，可以以 list 的方式提供，长度可以不同，也可以使用 2-D ndarray，每一列表示一组数据。

|参数|类型|说明|
|---|---|---|
|x|(n,) array or sequence of (n,) arrays|输入值。数组为数组 list，长度不需要相同|
|bins|int or sequence of str, optional|如果为 int 类型，则计算 `bins+1` 个 bin的边界，和 `numpy.histogram` 一致。


> 除了以上参数，该函数还可以包含一个 `data` 关键字参数。如果提供了 `data` 参数，则 'weights' 和 'X' 替换为 `data[<arg>]`。传递给 `data` 的对象必须支持访问操作 `data[<arg>]` 和成员测试操作 `<arg> in data`。