import plotly.graph_objects as go

fig = go.Figure(data=go.Contour(
    z=[[10, 10.625, 12.5, 15.625, 20],
       [5.625, 6.25, 8.125, 11.25, 15.625],
       [2.5, 3.125, 5., 8.125, 12.5],
       [0.625, 1.25, 3.125, 6.25, 10.625],
       [0, 0.625, 2.5, 5.625, 10]],
    colorbar=dict(nticks=10, ticks='outside',
                  ticklen=5, tickwidth=1,
                  showticklabels=True,
                  tickangle=0, tickfont_size=12)))

fig.show()
