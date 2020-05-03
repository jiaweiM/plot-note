import plotly.express as px
from skimage import data

img = data.astronaut()
fig = px.imshow(img)
fig.show()
