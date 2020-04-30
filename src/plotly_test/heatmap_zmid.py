import plotly.graph_objects as go

a = list(range(-10, 5))
b = list(range(-5, 10))
c = list(range(-5, 15))

fig = go.Figure(go.Heatmap(
    z=[a, b, c],
    colorscale='RdBu',
    zmid=5
))
fig.show()
