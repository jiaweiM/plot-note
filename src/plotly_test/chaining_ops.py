import plotly.express as px

df = px.data.iris()
(px.scatter(df, x="sepal_width", y="sepal_length", color="species",
            facet_col="species", trendline="ols", title="Iris Dataset")
    .update_layout(title_font_size=24)
    .update_xaxes(showgrid=False)
    .update_traces(
    line=dict(dash="dot", width=4),
    selector=dict(type="scatter", mode="lines"))
).show()
