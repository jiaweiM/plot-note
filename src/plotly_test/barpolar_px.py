import plotly.express as px

df = px.data.wind()  # 三维数据，风向，强度，频率

# 频率对应半径，角度对应风向，颜色对应强度
fig = px.bar_polar(df, r='frequency', theta='direction', color='strength',
                   template='plotly_dark', color_discrete_sequence=px.colors.sequential.Plasma_r)
fig.show()
