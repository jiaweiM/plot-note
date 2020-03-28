import plotly.express as px

df = px.data.tips()
df['size'] = df['size'].astype(str)
fig = px.scatter(df, x='total_bill', y='tip', color='size',
                 title="String 'size' values mean discrete colors")
fig.show()
