import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x='sepal_width', y='sepal_length', facet_col='species')
fig.update_yaxes(tick0=0.25, dtick=0.5)
fig.show()
