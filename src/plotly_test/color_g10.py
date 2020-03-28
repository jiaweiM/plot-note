import plotly.express as px

df = px.data.gapminder()
fig = px.line(df, y='lifeExp', x='year', color='continent', line_group='country', line_shape='spline',
              render_mode='svg', color_discrete_sequence=px.colors.qualitative.G10, title="Built-in G10 color sequence")
fig.show()
