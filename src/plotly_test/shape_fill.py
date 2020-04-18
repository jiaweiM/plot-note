import plotly.graph_objects as go

fig = go.Figure(
    go.Scatter(
        x=[0, 1, 2, 0],
        y=[0, 2, 0, 0],
        fill='toself'
    )
)
fig.show()
