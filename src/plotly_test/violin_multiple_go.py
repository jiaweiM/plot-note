import plotly.express as px
import plotly.graph_objects as go

df = px.data.tips()
fig = go.Figure()
days = ['Thur', 'Fri', "Sat", 'Sun']
for day in days:
    fig.add_trace(go.Violin(
        x=df['day'][df['day'] == day],
        y=df['total_bill'][df['day'] == day],
        name=day,
        box_visible=True,
        meanline_visible=True
    ))
fig.show()
