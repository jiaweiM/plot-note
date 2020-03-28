- [set_fontsize](#setfontsize)
- [set_fontweight](#setfontweight)
- [set_size](#setsize)

# set_fontsize
```
set_fontsize(self, fontsize)
```
字体大小，可以是绝对数值（size in points），也可以是相对默认字体大小的字符串。
- size in points
- 'xx-small'
- 'x-small'
- 'small'
- 'medium'
- 'large'
- 'x-large'
- 'xx-large'

# set_fontweight
```py
set_fontweight(self, weight)
```
设置文本字体粗细。

weight 取值
- 0-1000 的数值
- 'ultralight'
- 'light'
- 'normal'
- 'regular'
- 'book'
- 'medium'
- 'roman'
- 'semibold'
- 'demibold'
- 'demi'
- 'bold'
- 'heavy'
- 'extra bold'
- 'black'

# set_size
等效于 `set_fontsize`