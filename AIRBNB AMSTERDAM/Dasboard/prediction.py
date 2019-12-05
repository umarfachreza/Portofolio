import pickle
from numpy import around
from pandas import DataFrame,get_dummies
from sklearn.preprocessing import LabelEncoder
from datas import data_clean
import plotly
import plotly.express as px
import json

model = pickle.load(open('finalized_model.sav' , 'rb'))
real_columns = pickle.load(open('X_colomn.sav' , 'rb'))

def prediction(data):
    LE=LabelEncoder()
    df = DataFrame([data],columns=real_columns)    
    catagory_col =df.select_dtypes(include='O').columns
    dflabel=df.drop(catagory_col,axis=1)
    for item in catagory_col:
        dflabel[item]=LE.fit_transform(df[item])
    hasil = model.predict(dflabel)
    return around(hasil,decimals=2)

def Dist_harga_hasil(lokasi):
    df=data_clean()
    fig = px.histogram(df[df['neighbourhood_cleansed']==lokasi], x="price",title='Histogram of price in '+lokasi)
    fig_json=json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
