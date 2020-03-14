import plotly.graph_objects as go

large_rockwell_template = dict(
    layout=go.Layout(title_font=dict(family="Rockwell", size=24))
)

fig = go.Figure()
fig.update_layout(title='Figure Title', template=large_rockwell_template)
fig.show()
