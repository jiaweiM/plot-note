import plotly.graph_objects as go
import plotly.express as px

df = px.data.wind()  # 三维数据，风向，强度，频率

fig = go.Figure()

fig.add_trace(go.Barpolar(

))

# 频率对应半径，角度对应风向，颜色对应强度
fig = px.bar_polar(df, r='frequency', theta='direction', color='strength',
                   template='plotly_dark', color_discrete_sequence=px.colors.sequential.Plasma_r)
fig.show()
