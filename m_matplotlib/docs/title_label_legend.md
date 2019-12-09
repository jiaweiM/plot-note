
# Axis Labels, title, legend

|Method|Description|
|---|---|
|Axes.set_xlabel|Set the label for the x-axis.|
|Axes.get_xlabel|Get the xlabel text string.|
|Axes.set_ylabel|Set the label for the y-axis.|
|Axes.get_ylabel|Get the ylabel text string.|
|Axes.set_title|Set a title for the axes.|
|Axes.get_title|Get an axes title.|
|Axes.legend|Place a legend on the axes.|
|Axes.get_legend|Return the Legend instance, or None if no legend is defined.|
|Axes.get_legend_handles_labels|Return handles and labels for legend|

# legend
在图中添加 legend.
```py
Axes.legend(*args, **kwargs)
```
添加 legend 到 axes 中。

调用方法有三种：
- legend()
- legend(labels)
- legend(handles, labels)

## 自动检查
对方式1，legend 内容自动确定。

对这种方式，设置 legend 的方法有两种。
创建 plot 时指定 label:
```py
line, = ax.plot([1, 2, 3], label='Inline label')
ax.legend()
```

或者直接设置 label:
```py
line.set_label('Label via method')
line, = ax.plot([1, 2, 3])
ax.legend()
```
对这种方法，如果没有指定 label，就没有 legend。

## Legend 位置
legend 的位置可以通过 `loc` 关键字参数指定。

loc, int or string or pair of floats，默认值 `rcParams["legend.loc"]`，对 axes 为 'best'，对 figures 为 'upper right'。

|Location String|Location Code|
|---|---|
|`best`|0|
|`upper right`|1|
|`upper left`|2|
|`lower left`|3|
|`lower right`|4|
|`right`|5|
|`center left`|6|
|`center right`|7|
|`lower center`|8|
|`upper center`|9|
|`center`|10|

