import pandas as pd
import plotly.graph_objects as go
import omicsplot.sci_property as sci

data = pd.read_csv(r"Z:\MaoJiawei\glycosylation\liuluyao\round1_deltas.csv")
print(data)
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=data["Composition Ratio"],
    y=data['Marker Ratio'],
    mode='markers',
    marker=dict(
        symbol="square",
        size=10,
        color=data['Median Intensity'],
        showscale=True,
        opacity=0.7
    ),
    marker_line_width=0,
    text=data["Composition"]
))

fig.update_layout(
    xaxis_title="Composition Percentage",
    yaxis_title="Marker Percentage",
    template='plotly_white',
)

sci.update_property(fig)

fig.show()
fig.write_image(r"Z:\MaoJiawei\glycosylation\liuluyao\round1_deltas.svg")
