import plotly.express as px
import plotly.graph_objects as go

df = px.data.tips()

fig = go.Figure()
fig.add_trace(go.Violin(
    x=df['day'][df['sex'] == 'Male'],
    y=df['total_bill'][df['sex'] == 'Male'],
    legendgroup='M',
    scalegroup='M',
    name='M',
    line_color='blue'
))
fig.add_trace(go.Violin(
    x=df['day'][df['sex'] == 'Female'],
    y=df['total_bill'][df['sex'] == 'Female'],
    legendgroup='F',
    scalegroup='F',
    name='F',
    line_color='orange'
))
fig.update_traces(box_visible=True, meanline_visible=True, scalemode='count')
fig.update_layout(violinmode='group')
fig.show()
