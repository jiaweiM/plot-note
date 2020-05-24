import plotly.graph_objects as go
from plotly.subplots import make_subplots

labels = ["Specific", "Left Specific", "Right Specific", "Unspecific"]
titles = ["HeLa PSM", "Serum PSM", "HeLa Peptide", "Serum Peptide"]

fig = make_subplots(rows=2, cols=2,
                    subplot_titles=titles,
                    specs=[[{"type": "domain"}, {"type": "domain"}],
                           [{"type": "domain"}, {"type": "domain"}]])
hole_size = .3
# HeLa PSM
fig.add_trace(go.Pie(
    labels=labels,
    values=[19322, 1475, 3593, 1223],
    hole=hole_size
), row=1, col=1)

# HeLa Peptide
fig.add_trace(go.Pie(
    labels=labels,
    values=[14811, 1306, 3057, 1166],
    hole=hole_size
), row=1, col=2)


# Serum PSM
fig.add_trace(go.Pie(
    labels=labels,
    values=[6644, 849, 1887, 228],
    hole=hole_size
), row=2, col=1)

# Serum Peptide
fig.add_trace(go.Pie(
    labels=labels,
    values=[2343, 537, 1207, 186],
    hole=hole_size
), row=2, col=2)

fig.show()
fig.write_image(r"D:\data\semi\lly\donut.svg")
