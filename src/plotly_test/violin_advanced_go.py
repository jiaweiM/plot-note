import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = px.data.tips()

pointpos_male = [-0.9, -1.1, -0.6, -0.3]
pointpos_female = [0.45, 0.55, 1, 0.4]
show_legend = [True, False, False, False]

fig = go.Figure()
for i in range(0, len(pd.unique(df['day']))):
    fig.add_trace(go.Violin(
        x=df['day'][(df['sex'] == 'Male')
                    & (df['day'] == pd.unique(df['day'])[i])],
        y=df['total_bill'][(df['sex'] == 'Male')
                           & (df['day'] == pd.unique(df['day'])[i])],
        legendgroup='M',
        scalegroup='M',
        name='M',
        side='negative',
        pointpos=pointpos_male[i],  # 设置数据点相对 violin 的位置
        line_color='lightseagreen',
        showlegend=show_legend[i]
    ))
    fig.add_trace(go.Violin(
        x=df['day'][(df['sex'] == 'Female')
                    & (df['day'] == pd.unique(df['day'])[i])],
        y=df['total_bill'][(df['sex'] == 'Female')
                           & (df['day'] == pd.unique(df['day'])[i])],
        legendgroup='F',
        scalegroup='F',
        name='F',
        side='positive',
        pointpos=pointpos_female[i],  # 设置数据点相对 violin 的位置
        line_color='mediumpurple',
        showlegend=show_legend[i]
    ))

fig.update_traces(meanline_visible=True,
                  points='all',
                  jitter=0,
                  scalemode='count')
fig.update_layout(
    title_text='Total bill distribution<br><i>scaled by number of bills per gender',
    violingap=0,
    violingroupgap=0,
    violinmode='overlay'
)
fig.show()
