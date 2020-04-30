import plotly.express as px

df = px.data.tips()
fig = px.density_heatmap(df, x='total_bill', y='tip', title='Customized color bar on this density plot')
fig.update_layout(coloraxis_colorbar=dict(
    title='Number of Bills per Cell',
    thicknessmode='pixels', thickness=50,
    lenmode='pixels', len=200,
    yanchor='top', y=1,
    ticks='outside', ticksuffix=' bills',
    dtick=5
))
fig.show()
