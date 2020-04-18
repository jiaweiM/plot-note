import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x='sepal_width', y='sepal_length', facet_col='species')
fig.update_yaxes(nticks=20)
fig.show()
