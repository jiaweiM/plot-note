import numpy as np
import plotly.express as px

img_rgb = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
                    [[0, 255, 0], [0, 0, 255], [255, 0, 0]]
                    ], dtype=np.uint8)
fig = px.imshow(img_rgb)
fig.show()
