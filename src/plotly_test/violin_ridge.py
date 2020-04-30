import numpy as np
import plotly.graph_objects as go
from plotly.colors import n_colors

np.random.seed(1)
# 12 sets of normal distributed random data, with increasing mean and standard deviation
data = (np.linspace(1, 2, 12)[:, np.newaxis] * np.random.randn(12, 200) +
        (np.arange(12) + 2 * np.random.random(12))[:, np.newaxis])

colors = n_colors('rgb(5, 200, 200)', 'rgb(200, 10, 10)', 12, colortype='rgb')

fig = go.Figure()
for data_line, color in zip(data, colors):
    fig.add_trace(go.Violin(x=data_line, line_color=color))

fig.update_traces(orientation='h', side='positive', width=3, points=False)  # 只显示一半，才能有分布的效果
fig.update_layout(xaxis_showgrid=False, xaxis_zeroline=False)
fig.show()
