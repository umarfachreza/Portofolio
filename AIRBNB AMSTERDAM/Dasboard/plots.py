import plotly
import plotly.express as px
from datas import data_clean,clean_df1
import plotly.graph_objects as go
import json

def Dist_harga():
    df=data_clean()
    fig = px.box(df, x="neighbourhood_cleansed", y="price",title="Box Plot Price from Neighbourhood")
    fig_json=json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def Dist_harga1():
    df=data_clean()
    fig = px.histogram(df, x="price",title="Prices Distribution")
    fig_json=json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def Dist_harga2():
    df=data_clean()
    fig = go.Figure(data=[go.Pie(labels=df['neighbourhood_cleansed'].value_counts().index, 
                                 values=df['neighbourhood_cleansed'].value_counts(), hole=.3)],layout=go.Layout(
        title='persentasi neighbourhood cleansed',
        margin=go.Margin(l=0, r=200, b=100, t=100, pad=4)   # Margins - Left, Right, Top Bottom, Padding
        ))
    fig_json=json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def Dist_harga3():
    df=data_clean()
    series_neigh_price = df.groupby('neighbourhood_cleansed').mean()['price'].sort_values()
    fig=go.Figure([go.Bar(x=series_neigh_price.index, y=series_neigh_price)],layout=go.Layout(title='Mean Price from Location'))
    fig_json=json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def Dist_harga4():
    df_clean=clean_df1()
    fig = px.scatter_mapbox(df_clean, lat="latitude", lon="longitude", color='neighbourhood_cleansed', zoom=8, height=450)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig_json=json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
