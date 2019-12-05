import pandas as pd

location = ['Oostelijk Havengebied - Indische Buurt', 'Westerpark',
       'Centrum-Oost', 'Centrum-West', 'Bos en Lommer', 'Zuid',
       'De Pijp - Rivierenbuurt', 'De Baarsjes - Oud-West', 'Oud-Oost',
       'Slotervaart', 'Gaasperdam - Driemond', 'Noord-Oost',
       'Watergraafsmeer', 'Oud-Noord', 'Geuzenveld - Slotermeer',
       'Buitenveldert - Zuidas', 'IJburg - Zeeburgereiland', 'Noord-West',
       'De Aker - Nieuw Sloten', 'Osdorp', 'Bijlmer-Centrum',
       'Bijlmer-Oost']
property_type = ['Apartment', 'Townhouse', 'Houseboat', 'Bed and breakfast','Guest suite', 'Loft', 'Boat', 'Other', 'House', 'Condominium']
room_type =['Private room', 'Entire home/apt', 'Shared room']
cancel = ['strict', 'moderate', 'flexible']


def data_clean():
    df = pd.read_csv('clean.csv')
    return df

def clean_df1():
    df = pd.read_csv('clean_df.csv')
    return df

def clean_df(lokasi):
    df = pd.read_csv('clean_df.csv')
    df=df[df['neighbourhood_cleansed']==lokasi].sort_values('price',ascending=False)
    return df[['name','property_type','price']].head(5)

def recom(REV_ID):
       reviews = pd.read_csv('clean_reviews.csv')
       data_login=reviews[reviews['reviewer_id']==REV_ID]
       return data_login

def get_recom_hotel(id_rev):
    reviews = pd.read_csv('clean_reviews.csv')
    df_sim1 = pd.read_csv('cleansim.csv')
    new_listing = pd.read_csv('clean_listing.csv')
    print(df_sim1.shape)
    print(new_listing.shape)
    index_similar=df_sim1[str(int(reviews[reviews.reviewer_id==id_rev].listing_id.iloc[0]))].sort_values(ascending=False).head(11).index
    print(index_similar)
    return new_listing.loc[index_similar][0:]

def get_recom_hotel1(id_rev,lok):
    reviews = pd.read_csv('clean_reviews.csv')
    df_sim1 = pd.read_csv('cleansim.csv')
    new_listing = pd.read_csv('clean_listing.csv')
    print(df_sim1.shape)
    print(new_listing.shape)
    index_similar=df_sim1[df_sim1['loc']==lok][str(int(reviews[reviews.reviewer_id==id_rev].listing_id.iloc[0]))].sort_values(ascending=False).head(11).index
    print(index_similar)
    return new_listing.loc[index_similar][0:]


