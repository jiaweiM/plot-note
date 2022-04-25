import pandas as pd

import dash_bio

df = pd.read_csv(r'D:\repo\dash-bio-docs-files-master\volcano_data1.csv')

dash_bio.VolcanoPlot(
    dataframe=df,
)

