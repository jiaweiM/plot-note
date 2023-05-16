import plotly.express as px

df = px.data.wind()
fig = px.bar_polar(df, r="frequency", theta="direction",
                   color="strength", color_discrete_sequence=px.colors.sequential.Plasma_r)
fig.show()
