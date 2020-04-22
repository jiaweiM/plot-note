import plotly.express as px

df = px.data.tips()
print(df)
fig = px.bar(df, x='sex', y='total_bill', color='smoker', barmode='group', height=400)
fig.show()
