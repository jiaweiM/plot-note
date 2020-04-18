import plotly.express as px

fig = px.line(y=[1, 0])
fig.update_xaxes(showgrid=False, zeroline=False)
fig.update_yaxes(showgrid=False, zeroline=False)
fig.show()
