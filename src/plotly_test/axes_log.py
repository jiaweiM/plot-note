import numpy as np
import plotly.express as px

x = np.arange(10)
fig = px.scatter(x=x, y=x ** 3, log_x=True, log_y=True)
fig.show()
