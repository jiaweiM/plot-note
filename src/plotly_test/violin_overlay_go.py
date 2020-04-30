import plotly.express as px
import plotly.graph_objects as go

df = px.data.tips()

fig = go.Figure()
fig.add_trace(go.Violin(
    x=df['day'][df['smoker'] == 'Yes'],
    y=df['total_bill'][df['smoker'] == 'Yes'],
    legendgroup='Yes',
    scalegroup='Yes',
    name='Yes',
    side='negative',
    line_color='blue'
))
fig.add_trace(go.Violin(
    x=df['day'][df['smoker'] == 'No'],
    y=df['total_bill'][df['smoker'] == 'No'],
    legendgroup='No',
    scalegroup='No',
    name='No',
    side='positive',
    line_color='orange'
))
fig.update_traces(meanline_visible=True)
fig.update_layout(violingap=0.5, violinmode='overlay')
fig.show()
