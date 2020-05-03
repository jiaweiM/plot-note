import numpy as np
import plotly.graph_objects as go

phi = (1 + np.sqrt(5)) / 2.  # golden ratio
xe = [0, 1, 1 + (1 / (phi ** 4)), 1 + (1 / (phi ** 3)), phi]
ye = [0, 1 / (phi ** 3), 1 / phi ** 3 + 1 / phi ** 4, 1 / (phi ** 2), 1]

# x, y 有五个值，均比 z 多一个，对应 cell 两边，所以大小不一致
z = [[13, 3, 3, 5],
     [13, 2, 1, 5],
     [13, 10, 11, 12],
     [13, 8, 8, 8]]

fig = go.Figure(data=go.Heatmap(
    x=np.sort(xe),
    y=np.sort(ye),
    z=z,
    colorscale='Viridis'
))


# 添加样条线
def spiral(th):
    a = 1.120529
    b = 0.306349
    r = a * np.exp(-b * th)
    return r * np.cos(th), r * np.sin(th)


theta = np.linspace(-np.pi / 13, 4 * np.pi, 1000)  # angle
(x, y) = spiral(theta)

fig.add_trace(go.Scatter(x=-x + x[0], y=y - y[0],
                         line=dict(color='white', width=3)))

axis_template = dict(range=[0, 1.6], autorange=False,
                     showgrid=False, zeroline=False,
                     linecolor='black', showticklabels=False,
                     ticks='')

fig.update_layout(margin=dict(t=200, r=200, b=200, l=200),
                  xaxis=axis_template,
                  yaxis=axis_template,
                  showlegend=False,
                  width=700, height=700,
                  autosize=False)

fig.show()
