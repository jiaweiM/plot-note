# TOC
- [TOC](#toc)
- [GridSpec 使用](#gridspec-%e4%bd%bf%e7%94%a8)
  - [基础入门](#%e5%9f%ba%e7%a1%80%e5%85%a5%e9%97%a8)
    - [subplots](#subplots)
    - [GridSpec](#gridspec)
    - [Figure.add_gridspec](#figureaddgridspec)
    - [width_ratios & height_ratios](#widthratios--heightratios)
    - [subplots & gridspec](#subplots--gridspec)
  - [精细调整 Gridspec](#%e7%b2%be%e7%bb%86%e8%b0%83%e6%95%b4-gridspec)
  - [GridSpec & SubplotSpec](#gridspec--subplotspec)
  - [内嵌 GridSpec](#%e5%86%85%e5%b5%8c-gridspec)
# GridSpec 使用
GridSpec 使用网格形式布局多个 `Axes`。

用于创建网格形式的布局：
|方法|说明|
|---|---|
|`subplots()`|用于创建 figure 和 axes 的基础函数。类似于 `pyplot.subplot()`，但是一次性创建并布置所有的 axes|
|`GridSpec`|指定放置 subplot 的网格。需要设置网格的行数和列数，也可以设置其它参数|
|`SubplotSpec`|指定 subplot 在 `GridSpec` 中的位置|
|`subplot2grid`|类似于 `subplot()` 函数，但是使用 0-based 索引，必须允许一个 subplot 占据多个 cells|

## 基础入门
下面演示使用 `subplots()` 和 gridspec 创建一个 $2\times2$ 的网格。

### subplots
使用 `subplots()` 十分简单，该函数返回 `Figure` 实例和 `Axes` 对象数组。
```py
import matplotlib.pyplot as plt
fig1, f1_axes = plt.subplots(ncols=2, nrows=2, constrained_layout=True)
plt.show()
```
效果如下：

![](images/gridspec_1.png)


### GridSpec
对于简单的情况，如这个例子，使用 `gridspec` 会显得很繁琐。需要单独创建 figure 和 `GridSpec`，然后将 gridspec 实例传递给 `add_subplot()` 方法创建 axes 对象。访问 gridspec 元素的方法和访问 numpy 数组元素的方法一样。
```py
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt

fig = plt.figure(constrained_layout=True)
spec = gridspec.GridSpec(ncols=2, nrows=2, figure=fig)
fig_ax1 = fig.add_subplot(spec[0, 0])
fig_ax2 = fig.add_subplot(spec[0, 1])
fig_ax3 = fig.add_subplot(spec[1, 0])
fig_ax4 = fig.add_subplot(spec[1, 1])

plt.show()
```
效果如下：

![](images/gridspec_2.png)

### Figure.add_gridspec
gridspec 的优点在于一个 subplot 可以占据多个 rows 和 columns。选择 subplot 占据的位置的语法类似于 numpy slice。

另外，可以使用 `Figure.add_gridspec` 而不是 `gridspec.GridSpec`，这样更为简便，可以避免导入 `gridspec`。例如：
```py
import matplotlib.pyplot as plt

fig = plt.figure(constrained_layout=True)
gs = fig.add_gridspec(3, 3)
fig_ax1 = fig.add_subplot(gs[0, :])
fig_ax1.set_title('gs[0, :]')
fig_ax2 = fig.add_subplot(gs[1, :-1])
fig_ax2.set_title('gs[1:, :-1]')
fig_ax3 = fig.add_subplot(gs[1:, -1])
fig_ax3.set_title('gs[1:, -1]')
fig_ax4 = fig.add_subplot(gs[-1, 0])
fig_ax4.set_title('gs[-1, 0]')
fig_ax5 = fig.add_subplot(gs[-1, -2])
fig_ax5.set_title('gs[-1, -2]')

plt.show()
```
效果：

![](images/gridspec_3.png)

`gridspec` 在创建不同宽度的 subplots 中必不可少。下面的方法和上面类似，每个 cell 大小都设置为1，因此大小相同：
```py
import matplotlib.pyplot as plt

fig = plt.figure(constrained_layout=True)
spec = fig.add_gridspec(ncols=2, nrows=2)
anno_opts = dict(xy=(0.5, 0.5), xycoords='axes fraction',
                 va='center', ha='center')

ax1 = fig.add_subplot(spec[0, 0])
ax1.annotate('GridSpec[0, 0]', **anno_opts)
fig.add_subplot(spec[0, 1]).annotate('GridSpec[0, 1]', **anno_opts)
fig.add_subplot(spec[1, 0]).annotate('GridSpec[1, 0]', **anno_opts)
fig.add_subplot(spec[1, 1]).annotate('GridSpec[1, 1]', **anno_opts)

plt.show()
```

效果：

![](images/gridspec_4.png)


### width_ratios & height_ratios
另一个选择是使用 `width_ratios` 和 `height_ratios` 参数，指定不同行和列占据的比例。而且使用的是相对值，即 `width_ratios=[2, 4, 8]` 等价于 `width_ratios=[1, 2, 4]`。
```py
import matplotlib.pyplot as plt

fig = plt.figure(constrained_layout=True)
widths = [2, 3, 1.5]
heights = [1, 3, 2]

spec = fig.add_gridspec(ncols=3, nrows=3, width_ratios=widths, height_ratios=heights)
for row in range(3):
    for col in range(3):
        ax = fig.add_subplot(spec[row, col])
        label = 'Width: {}\nHeight: {}'.format(widths[col], heights[row])
        ax.annotate(label, (0.1, 0.5), xycoords='axes fraction', va='center')
plt.show()
```

效果：

![](images/gridspec_5.png)

### subplots & gridspec
`subplots` 和 `gridspec` 方法也可以组合起来使用，毕竟使用 `subplots` 更为方便。可以先使用 `subplots` 创建，然后移除或合并部分。例如，下面将最后一列的下面两个网格合并：
```py
import matplotlib.pyplot as plt

fig, axs = plt.subplots(ncols=3, nrows=3)
gs = axs[1, 2].get_gridspec()

# remove the underlying axes
for ax in axs[1:, -1]:
    ax.remove()

axbig = fig.add_subplot(gs[1:, -1])
axbig.annotate('Big Axes \nGridSpec[1:, -1]', (0.1, 0.5), xycoords='axes fraction', va='center')
fig.tight_layout()

plt.show()
```

效果：

![](images/gridspec_6.png)


## 精细调整 Gridspec
使用 `GridSpec`可以调整 subplots 的布局参数。

> 注意：这些参数选项和 `constrained_layout` 或 `Figure.tight_layout` 不兼容，这两方法都会调整 subplot 大小以填充 figure。

示例：
```py
import matplotlib.pyplot as plt

fig = plt.figure(constrained_layout=False)
gs = fig.add_gridspec(nrows=3, ncols=3, left=0.05, right=0.48, wspace=0.05)

ax1 = fig.add_subplot(gs[:-1, :])
ax2 = fig.add_subplot(gs[-1, :-1])
ax3 = fig.add_subplot(gs[-1, -1])

plt.show()
```

效果：

![](images/gridspec_7.png)

这类似于`subplots_adjust()`，但是只针对指定 `GridSpec` 中的 subplots。

例如，创建左右两个 `GridSpec`:
```py
import matplotlib.pyplot as plt

fig = plt.figure(constrained_layout=False)
gs1 = fig.add_gridspec(nrows=3, ncols=3, left=0.05, right=0.48, wspace=0.05)

ax1 = fig.add_subplot(gs1[:-1, :])
ax2 = fig.add_subplot(gs1[-1, :-1])
ax3 = fig.add_subplot(gs1[-1, -1])

gs2 = fig.add_gridspec(nrows=3, ncols=3, left=0.55, right=0.98, hspace=0.05)
fig.add_subplot(gs2[:, :-1])
fig.add_subplot(gs2[:-1, -1])
fig.add_subplot(gs2[-1, -1])

plt.show()
```
效果：

![](images/gridspec_8.png)

## GridSpec & SubplotSpec
可以使用 `SubplotSpec` 构建 `GridSpec`，

## 内嵌 GridSpec
下面是一个更为复杂的例子，