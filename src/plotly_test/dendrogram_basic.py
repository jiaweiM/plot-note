import numpy as np
import plotly.figure_factory as ff

np.random.seed(1)

X = np.random.rand(15, 12)  # 15 samples, with 12 dimensions each
print(X)
fig = ff.create_dendrogram(X)
fig.update_layout(width=800, height=500)
fig.show()
