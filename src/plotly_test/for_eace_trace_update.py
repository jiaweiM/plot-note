import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
fig.for_each_trace(
    lambda trace: trace.update(name=trace.name.replace('=', ': ')),
)
fig.show()
