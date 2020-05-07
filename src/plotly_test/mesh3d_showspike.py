import numpy as np
import plotly.graph_objects as go

N = 50
fig = go.Figure(data=[go.Mesh3d(x=(30 * np.random.randn(N)),
                                y=(25 * np.random.randn(N)),
                                z=(30 * np.random.randn(N)),
                                opacity=0.5, )])
fig.update_layout(scene=dict(xaxis_showspikes=False,
                             yaxis_showspikes=False))
fig.show()
