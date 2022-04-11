import plotly.express as px
import matplotlib.pyplot as plt

data = px.data.iris()

fig, ax = plt.subplots()
species = ["setosa", "virginica", "versicolor"]
markers = ["d", "v", "s"]
colors = ['red', 'green', 'blue']

for s, m, c in zip(species, markers, colors):
    ax.scatter(x="sepal_width", y="sepal_length", data=data[data["species"] == s],
               c=c, marker=m)

plt.show()
