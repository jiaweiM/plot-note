# Layout

- [Layout](#layout)
  - [uniformtext](#uniformtext)
    - [showlegend](#showlegend)

***

`title_text`, 标题文本。

## uniformtext

包含下面参数的 dict.

- mode

Type: {False, "hide", "show"}

如果计算的文本尺寸小于 `uniformtext.minsize` 设置的最小尺寸的处理方式。

"hide" 表示隐藏文本。

"show" 显示文本，但不进一步缩小文本。

如果 `minsize` 大于 trace 定义的字体大小，使用 `minsize`。

- minsize

默认 0。

最小文本大小。

### showlegend

parent: `layout`

Type: boolean

是否显示 legend。如果有一个 trace，并满足如下任意条件，默认为 `True`:

- 包含两个或多个 trace
- 有 pie trace
- 显式设置 `showlegend:True`
