import plotly.express as px

df = px.data.tips()
fig = px.scatter(df, x='total_bill', y='tip', facet_col='sex', width=1000, height=600)
fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightSteelBlue",
)

fig.show()
