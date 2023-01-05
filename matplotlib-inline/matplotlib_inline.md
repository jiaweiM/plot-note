# Matplotlib Inline

Last updated: 2023-01-05, 13:13
****

## 简介

该包用于在 Jupyter 中内嵌显示 matplotlib 图像。

在当前 JupyterLab 和 Jupyter Notebook 版本中，不需要显式使用 `%matplotlib inline` 指令，其它第三方客户端可能仍然需要。

例如：

```python
%matplotlib inline

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3*np.pi, 500)
plt.plot(x, np.sin(x**2))
plt.title('A simple chirp');
```

会直接在下方显示 figure。

## API

```python
set_matplotlib_formats(*formats, **kwargs)
```

设置 inline 后端图形格式。还可以为 JPEG 设置图形质量。参数：

- `*formats`: strs

设置一种或多种图形格式：'png', 'retina', 'jpeg', 'svg', 'pdf'。

- `**kwargs`

关键字参数，被转发到 `figure.canvas.print_figure`。

例如，设置输出 PNG 和 JPEG，并将 JPEG 质量设置为 90%:

```python
from matplotlib_inline import backend_inline

backend_inline.set_matplotlib_formats('png', 'jpeg', quality=90)
```


## 参考

- https://github.com/ipython/matplotlib-inline
