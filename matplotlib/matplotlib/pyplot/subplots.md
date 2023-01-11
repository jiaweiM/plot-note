# matplotlib.pyplot.subplots

Last updated: 2023-01-05, 19:45
****

```python
matplotlib.pyplot.subplots(
    nrows=1, ncols=1, *, 
    sharex=False, sharey=False, 
    squeeze=True, 
    width_ratios=None, height_ratios=None, 
    subplot_kw=None, 
    gridspec_kw=None, 
    **fig_kw)
```

创建一个 figure 和一组 subplots。

该方法可以方便地创建常见子图布局。

## 参数

**nrows, ncols**： `int`, default: 1

子图网格的行数和列数。

**sharex, sharey**: `bool` or {'none', 'all', 'row', 'col'}, default: False

控制 x 轴和 y 轴的共享属性：

- True 或 'all': 所有子图共享 x 轴或 y 轴
- False 或 'none'：子图的x 轴或 y 轴互相独立
- 'row': 每一行子图共享 x 轴或 y 轴
- 'col'：每一列子图共享 x 轴或 y 轴

当每一列子图共享 x 轴，只创建底部子图的 x 刻度标签。类似地，当每一行子图共享 y 轴，只创建第一列子图的 y 轴刻度标签。可以使用 `tick_params` 启用其它子图的刻度标签。

当子图共享的轴带有单位，使用 `set_units` 设置新的单位。

**squeeze**: `bool`, default: `True`

- `True` 表示从返回的 `Axes` 数组剔除额外的维度
  - 如果只创建一个 subplot (nrows=ncols=1)，以标量形式返回一个 Axes 对象
  - 对 Nx1 或 1xM subplots，返回 Axes 对象的 1D numpy 数组
  - 对 NxM subplots，且 N>1, M>1，返回 2D 数组
- `False` 表示不剔除额外维度，总是 `Axes` 对象的二维数组，即使是 1x1 数组

**width_ratios**: array-like of length ncols, optional

定义 columns 的相对宽度。每个 column 的相对宽度为 `width_ratios[i] / sum(width_ratios)`。如果不设置，所有 column 宽度相同。等价于 `gridspec_kw={'width_ratios': [...]}`。

**height_ratios**: array-like of length nrows, optional

定义 rows 的相对高度。每个 row 的相对高度为 `height_ratios[i] / sum(height_ratios)`。如果不设置，所有 rows 高度相同。等价于 `gridspec_kw={'height_ratios': [...]}`。

**subplot_kw**: `dict`, optional

包含关键字的 dict，传递给 `add_subplot` 创建 subplot。

**gridspec_kw**: `dict`, optional

包含关键字参数的 dict，传递给 `GridSpec` 构造函数创建网格。

****fig_kw**

传递给 `pyplot.figure` 的额外关键字参数。

## 返回

**fig**: `Figure`

**ax**: `Axes` or array of `Axes`

创建单个 subplot 时，`ax` 是单个 `Axes` 对象，创建多个 subplot 时，`ax` 是 `Axes` 数组。返回数组的维度可以用 `squeeze` 参数控制。

处理返回值的惯用方法：

```python
# 对单个 Axes 用 ax 变量名
fig, ax = plt.subplots()

# 对多个 Axes 用 axs 变量名
fig, axs = plt.subplots(2, 2)

# 对多个 Axes 用 tuple 解包
fig, (ax1, ax2) = plt.subplots(1, 2)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
```

## 示例

```python
# 创建示例数据
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# 创建一个 figure 和一个 subplot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple plot')

# 创建 2 个 subplot 并直接解包
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)

# 创建 4 个 polar axes，并通过返回的数据访问
fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
axs[0, 0].plot(x, y)
axs[1, 1].scatter(x, y)

# 每列 subplot 共享 X 轴
plt.subplots(2, 2, sharex='col')

# 每行 subplot 共享 Y 轴
plt.subplots(2, 2, sharey='row')

# 所有 subplot 共享 X 轴和 Y 轴
plt.subplots(2, 2, sharex='all', sharey='all')

# 共享 X 轴和 Y 轴
plt.subplots(2, 2, sharex=True, sharey=True)

# 创建包含 1 个 subplot 编号为 10 的 figure，如果已存在，则清除
# num 和 clear 传递给 pyplot.figure
fig, ax = plt.subplots(num=10, clear=True)
```

## 参考

- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html
