import plotly.graph_objects as go
import numpy as np

fig = go.Figure(data=go.Scatter(
    y=np.random.randn(500),  # 500 个数据点
    mode='markers',
    marker=dict(
        size=16,
        color=np.random.randn(500),  # set color equal to a variable
        colorscale='Viridis',  # one of plotly colorscales
        showscale=True
    )
))

fig.show()
