import plotly.express as px
import plotly.graph_objects as go

iris = px.data.iris()
fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species")
fig.add_trace(
    go.Scatter(
        x=[2, 4],
        y=[4, 8],
        mode="lines",
        line_color="gray",
        # line=go.scatter.Line(color="gray"),
        showlegend=False)
)
fig.show()
