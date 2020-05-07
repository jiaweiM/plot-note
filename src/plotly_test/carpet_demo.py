import plotly.graph_objects as go

fig = go.Figure(go.Carpet(
    y=[2, 3.5, 4, 3, 4.5, 5, 5.5, 6.5, 7.5, 8, 8.5, 10]
))

fig.show()
