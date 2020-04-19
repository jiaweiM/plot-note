import plotly.graph_objects as go
import numpy as np

# Generate data
x0 = np.linspace(1, 3, 200)
y0 = x0 * np.sin(np.power(x0, 2)) + 1

# Create figure with scatter trace
fig = go.Figure()

fig.add_trace(go.Scatter(x=x0, y=y0, ))

# Set title text
fig.update_layout(
    title_text="$f(x)=x\\sin(x^2)+1\\\\ f\'(x)=\\sin(x^2)+2x^2\\cos(x^2)$"
)

# Add tangent line shapes
fig.add_shape(
    type="line",
    x0=1,
    y0=2.30756,
    x1=1.75,
    y1=2.30756,
)
fig.add_shape(
    type="line",
    x0=2.5,
    y0=3.80796,
    x1=3.05,
    y1=3.80796,
)
fig.add_shape(
    type="line",
    x0=1.90,
    y0=-1.1827,
    x1=2.50,
    y1=-1.1827,
)
fig.update_shapes(dict(
    xref="x",
    yref="y",
    opacity=0.7,
    line=dict(
        color="Crimson",
        width=2.5,
    )))
fig.show()
