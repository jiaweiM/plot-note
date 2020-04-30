import plotly.express as px
import plotly.graph_objects as go

df = px.data.tips()
fig = go.Figure()
fig.add_trace(go.Violin(
    y=df['tip'],
    x=df['smoker'],
    scalemode="count"
))
fig.show()
