import plotly.express as px

df = px.data.tips()
fig = px.density_heatmap(df, x='total_bill', y='tip', title='No color bar on this density plot')
fig.update_layout(coloraxis_showscale=False)
fig.show()
