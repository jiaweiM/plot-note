# 颜色

- [颜色](#颜色)
  - [指定颜色](#指定颜色)
  - [参考](#参考)

2022-01-06, 13:24
***

## 指定颜色

Matplotlib 识别如下格式的颜色。

- RGB or RGBA (red, green, blue, alpha) tuple of float values in a closed interval [0, 1].

例如：`(0.1, 0.2, 0.5)`, `(0.1, 0.2, 0.5, 0.3)`

- Case-insensitive hex RGB or RGBA string.

例如 `'#0f0f0f'`, `'#0f0f0f80'`

- Case-insensitive RGB or RGBA string equivalent hex shorthand of duplicated characters.

例如： `'#abc'` as `'#aabbcc'`，`'#fb1'` as `'#ffbb11'`

- String representation of float value in closed interval [0, 1] for grayscale values.

例如：'0' as black，'1' as white，'0.8' as light gray


## 参考

- https://matplotlib.org/stable/tutorials/colors/colors.html
