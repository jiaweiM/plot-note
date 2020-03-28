import plotly.express as px

df = px.data.tips()
df['size'] = df['size'].astype(str)  # 转换为字符串
df['size'] = df['size'].astype(float)  # 重新转换为数值

fig = px.scatter(df, x='total_bill', y='tip', color='size',
                 title="Numeric 'size' values mean continous color")
fig.show()
