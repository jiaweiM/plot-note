import plotly.express as px
import plotly.graph_objects as go

df = px.data.tips()

fig = go.Figure(
    go.Violin(
        y=df['total_bill'],
        box_visible=True,
        line_color='black',
        meanline_visible=True,
        fillcolor='lightseagreen',
        opacity=0.6,
        x0='Total Bill'
    )
)
fig.update_layout(yaxis_zeroline=False)
fig.show()
