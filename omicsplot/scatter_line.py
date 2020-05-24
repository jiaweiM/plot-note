import pathlib

import pandas as pd
import plotly.graph_objects as go

out_folder = r'D:\data\test'
file_name = 'd1.svg'
out = pathlib.PurePath(out_folder) / file_name
df = pd.read_excel(r"D:\data\test\eight-time point BIO5 insulin-regulated proteins.xlsx", sheet_name=0)
# genes = ['FUS', 'EWSR1']
# dtick = 0.5
# genes = ['TNFRSF10B', 'TNFRSF10D']
# genes = ['CPD', 'IGF2R', "LRP1", "TFRC"]
# genes = ['ADCY9', 'CNNM3', "PODXL2"]
# genes = ['CTNNB1', 'CTNND1']
genes = ['IGF2R', 'LNPEP', 'LRP1', 'TFRC', 'SORT1']
# genes = ['CPD', 'ECE1', 'HFE', 'LDLR', 'LRP8', 'MRC2']

# 左下
# l_x = 0.02
# l_y = 0.1

# 左下下
# l_x = 0.02
# l_y = 0.02

# 右上
# l_x = 0.7
# l_y = 0.9

# 右上上
# l_x = 0.7
# l_y = 1

# 左上
# l_x = 0.02  # 默认值
# l_y = 1.02

# 外侧
l_x = 1.02
l_y = 1.02

# genes = ['CAV1', 'CAV2']
# genes = ['CAP1', 'CAP2']
# genes = ['FUS', 'HNRNPA2B1', 'HNRNPD', 'PRPF40A', 'SF1', 'SF3B5', 'RBMX;RBMXL1']
# genes = ['CPD', 'ECE1', 'HFE', 'LDLR', 'LRP8', 'MRC2']
# genes = ['EIF4E']
# genes = ['LOXL2']
# genes = ['MARCKS']
# genes = ['AGRN']
# genes = ['CLIC4', 'NIP7']
# genes = ['ATP6V0A2']
# genes = ['GLG1']
# genes = ['GOLGA2']
# genes = ['IGF2R', 'LNPEP', 'LRP1', 'SORT1', 'TFRC']
# genes = ['ACAT2', 'CYP51A1', 'DHCR24', 'FDFT1', 'HMGCS1', 'MSMO1', 'SQLE']
# genes = ['ACLY', 'DHCR7', 'FDPS', 'HSD17B7', 'IDI1', 'LSS', 'NSDHL']
# genes = ['ACLY', 'FASN']
# genes = ['INSR', 'IGF1R']
# genes = ['CAV1', 'CAV2']
# genes = ['CTNNB1', 'CTNND1']
# genes = ['FUS', 'EWSR1']

gene_column = 'Gene names'
# gene_column = 'T: Gene names'
gene_frame = df[df[gene_column].map(lambda g: g in genes)]
gene_index_frame = gene_frame.set_index(gene_column)

# columns = ['CTRL', '10s', '30s', '2min', '5min', '30min', '2h', '12h', '24h']
# columns = ['ctrl', 'FC Median-30min', 'FC Median-2h', 'FC Median-12h', 'FC Median-24h']
# columns = ['ctrl', 'Median: 10s vs ctrl', 'Median:30s vs ctrl', 'Median:2min vs ctrl', 'Median:5min vs ctrl',
#            'Median: 30min vs ctrl']

columns = ['CTRL', '10s', '30s', '2min', '5min', '30min', '2h', '12h', '24h']
rsds = ['RSD-CTRL', 'RSD-10s', 'RSD-30s', 'RSD-2min', 'RSD-5min', 'RSD-30min', 'RSD-2h', 'RSD-12h', 'RSD-24h']
# rsds = ['Error bar-ctrl', 'Error bar-30min', 'Error bar-2h', 'Error bar-12h', 'Error bar-24h']
# rsds = [0, 'Error bar-10s', 'Error bar-30s', 'Error bar-2min', 'Error bar-5min', 'Error bar-30min']

x = ['0', '10s', '30s', '2min', '5min', '30min', '2h', '12h', '24h']
# x = ['0', '0.5', '2', '12', '24']
# x = ['0', '0.17', '0.5', '2', '5', '30']

# title = 'Time of insulin exposure'
# title = 'Time of insulin exposure (h)'
title = 'Time of insulin exposure (min)'

fig = go.Figure()

for gene in genes:
    gene_data = gene_index_frame.xs(gene)
    # print(gene_data)
    gene_values = gene_data.loc[columns]
    gene_rsds = gene_data.loc[rsds]
    fig.add_trace(go.Scatter(
        x=x,
        y=gene_values,
        error_y=dict(
            type='data',
            array=gene_rsds,
            visible=True,
            color="GRAY",
            thickness=1
        ),
        mode='lines+markers',
        name=gene,
        line_width=2,
    ))

title_font_size = 35
tick_font_size = 28
font_family = "Arial Narrow Bold"

fig.update_layout(
    xaxis_type='category',
    xaxis_title=title,
    yaxis_title="Fold change",
    template='plotly_white',
    showlegend=True,
    legend=dict(x=l_x, y=l_y,
                font=dict(
                    family=font_family,
                    size=tick_font_size,
                    color='black')
                )
)

fig.update_xaxes(title_font=dict(
    family=font_family,
    size=title_font_size,
    color='black'),
    title_standoff=2,
    showline=True,
    linecolor='gray',
    mirror=True,
    showgrid=False,
    ticks='outside',
    tickangle=45,
    tickfont=dict(
        family=font_family,
        color='black',
        size=tick_font_size
    )
)
fig.update_yaxes(title_font=dict(
    family=font_family,
    size=title_font_size,
    color='black'),
    title_standoff=10,
    showline=True,
    linecolor='gray',
    mirror=True,
    showgrid=False,
    ticks='outside',
    # tick0=0,
    # dtick=dtick,
    rangemode='tozero',
    tickfont=dict(
        family=font_family,
        color='black',
        size=tick_font_size
    )
)
fig.update_traces(marker_size=12)
fig.show()
fig.write_image(str(out))
