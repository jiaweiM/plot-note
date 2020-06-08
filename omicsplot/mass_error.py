import pandas as pd
import plotly.graph_objects as go

data = pd.read_excel(r"D:\data\semi\zhang_hui\kidney\mass error.xlsx", index_col=None)
fig = go.Figure()
for id in data.columns:
    fig.add_trace(go.Violin(
        name=id,
        y=data[id],
        box_visible=True,
        # meanline_visible=True
    ))
# fig.update_layout()
fig.show()
