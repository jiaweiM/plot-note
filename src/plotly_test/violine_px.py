import plotly.express as px

df = px.data.tips()
print(df)
fig = px.violin(df, y='total_bill')
fig.show()


