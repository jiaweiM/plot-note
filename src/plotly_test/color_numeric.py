import plotly.express as px

df = px.data.tips()
fig = px.scatter(df, x='total_bill', y='tip', color='size',
                 title="Numeric 'size' values mean continous color")
fig.show()
