import plotly.offline as py
import pandas as pd

def us_choropleth(locations,values,bar_title,title):
    data = [dict(type = "choropleth",
                 locations = locations,
                 z = values,
                 locationmode = "USA-states",
                 marker = dict(line=dict(width=1.25)),
                 colorbar = dict(title=bar_title))]

    layout = dict(title = title,
                  geo = dict(scope = "usa",
                             projection = dict(type="albers usa"),
                             showlakes = True,
                             lakecolor = "rgb(255,255,255)"))

    fig = dict(data=data,layout=layout)
    return fig

def show_plot(fig,filename):
    py.plot(fig,filename=filename)