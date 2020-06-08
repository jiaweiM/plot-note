import plotly.express as px

df = px.data.iris()
print(df)
df.to_csv(r"D:\data\test\a.csv")
print(type(df))