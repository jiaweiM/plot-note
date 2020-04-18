import plotly.express as px

fig = px.bar(x=[1, 2, 4, 10], y=[8, 6, 11, 5])
fig.update_layout(xaxis_type='category',
                  title_text="Bar chart with categorical axes")
fig.show()
