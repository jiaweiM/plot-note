import plotly.graph_objects as go

fig = go.Figure(data=go.Contour(
    z=[[10, 10.625, 12.5, 15.625, 20],
       [5.625, 6.25, 8.125, 11.25, 15.625],
       [2.5, 3.125, 5., 8.125, 12.5],
       [0.625, 1.25, 3.125, 6.25, 10.625],
       [0, 0.625, 2.5, 5.625, 10]],
    contours=dict(
        coloring='heatmap',
        showlabels=True,  # show labels on contours
        labelfont=dict(  # label font properties
            size=12,
            color='white',
        )
    )))

fig.show()
