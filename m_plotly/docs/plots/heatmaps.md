
# 基本热图
```py
import plotly.graph_objects as go

fig = go.Figure(data=go.Heatmap(
                    z=[[1, 20, 30],
                      [20, 1, 60],
                      [30, 60, 1]]))
fig.show()
```

其中z，提供了颜色相关的值。

效果：
![](images/plot1.png)

# 分类标签热图

