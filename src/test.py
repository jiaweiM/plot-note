import pandas as pd
import dash_bio

df = pd.read_csv('https://git.io/volcano_data1.csv')

dash_bio.VolcanoPlot(
    dataframe=df,
)
