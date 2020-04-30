import numpy as np
import plotly.colors as pc
import plotly.graph_objects as go

np.random.seed(1)

data = (np.linspace(1, 2, 12)[:, np.newaxis] * np.random.randn(12, 200) +
        (np.arange(12) + 2 * np.random.random(12))[:, np.newaxis])
colors = pc.n_colors('rgb(5, 200, 200)', 'rgb(200, 10, 10)', 12, colortype='rgb')

fig = go.Figure()
for data_line, color in zip(data, colors):
    fig.add_trace(go.Violin(x=data_line, line_color=color))

fig.update_traces(orientation='h', side='positive', width=3, points=False)
fig.update_layout(xaxis_showgrid=False, xaxis_zeroline=False)
fig.show()
