def update_property(fig):
    fig.update_layout(
        template='plotly_white'
    )
    font = "Arial"
    size = 22
    tick_size = 18
    fig.update_xaxes(
        title_font=dict(
            family=font,
            color='black',
            size=size
        ),
        showline=True,
        linecolor='gray',
        mirror=True,
        zeroline=False,
        showgrid=False,
        ticks='outside',
        tickfont=dict(
            family=font,
            color='black',
            size=tick_size
        )
    )
    fig.update_yaxes(
        title_font=dict(
            family=font,
            color='black',
            size=size
        ),
        showline=True,
        linecolor='gray',
        mirror=True,
        zeroline=False,
        showgrid=False,
        ticks='outside',
        tickfont=dict(
            family=font,
            color='black',
            size=tick_size
        )
    )
