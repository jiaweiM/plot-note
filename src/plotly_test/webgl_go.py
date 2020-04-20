import numpy as np
import plotly.graph_objects as go

N = 100000

fig = go.Figure()

fig.add_trace(
    go.Scattergl(
        x=np.random.randn(N),
        y=np.random.randn(N),
        mode='markers',
        marker=dict(
            line=dict(
                width=1,
                color='DarkSlateGrey'
            )
        )
    )
)

fig.show()
