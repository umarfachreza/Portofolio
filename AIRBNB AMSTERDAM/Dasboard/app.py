from flask import Flask,render_template,request,redirect,url_for
from datas import location,property_type,cancel,room_type,get_recom_hotel,recom,get_recom_hotel1,clean_df,clean_df1
from prediction import prediction,Dist_harga_hasil
from plots import Dist_harga,Dist_harga1,Dist_harga2,Dist_harga3,Dist_harga4

app = Flask(__name__)

@app.route('/prediction',methods= ["GET","POST"])
def index():
    if request.method == "POST" :
        #kita jalankan function predict then kita render result.html
        # location = request.form['location']
        # rooms = request.form['rooms']
        # bathrooms = request.form['bathroom']
        # size = request.form['size']
        data = request.form
        data = data.to_dict()
        data['accommodates'] = int(data['accommodates'])
        data['bathrooms'] = int(data['bathrooms'])
        data['bedrooms'] = int(data['bedrooms'])
        data['beds'] = int(data['beds'])
        data['guests_included'] = int(data['guests_included'])
        # data['extra_people'] = int(data['extra_people'])
        data['security_deposit'] = int(data['security_deposit'])
        # data['availability_365'] = int(data['availability_365'])
        # data['new_Hairdryer'] = int(data['new_Hairdryer'])
        data['new_Kitchen'] = int(data['new_Kitchen'])
        data['new_Laptopfriendlyworkspace'] = int(data['new_Laptopfriendlyworkspace'])
        data['new_Indoorfireplace'] = int(data['new_Indoorfireplace'])
        data['new_Hottub'] = int(data['new_Hottub'])
        data['new_baby_friendly'] = int(data['new_baby_friendly'])
        data['new_Iron'] = int(data['new_Iron'])
        data['new_TV'] = int(data['new_TV'])
        data['new_family'] = int(data['new_family'])

        hasil = prediction(data)
        dist=Dist_harga_hasil(data['neighbourhood_cleansed'])
        table=clean_df(data['neighbourhood_cleansed'])
        return render_template('result.html' , hasil_pred=hasil[0],dist=dist,table=table)
    return render_template('prediction.html',data_location=sorted(location),property_type=sorted(property_type),cancel=sorted(cancel),room=sorted(room_type))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods= ["GET","POST"])
def login():
    if request.method == "POST" :
        data = request.form
        data = data.to_dict()
        id_rev = int(data['reviews_id'])
        # hasil=get_recom_hotel(id_rev)
        # login=recom(id_rev)
        return redirect(url_for('welcome',idr=id_rev))
        # return redire('result_login.html' , hasil_pred=hasil, login=login)
    return render_template('login.html')

@app.route('/welcome' , methods=['GET','POST'])
def welcome():
    if(request.method == 'POST'):
        data = request.form
        data = data.to_dict()
        lokasi = (data['neighbourhood_cleansed'])
        id = request.args['idr']
        id = int(id)
        hasil=get_recom_hotel1(id,lokasi)
        login=recom(id)
        return render_template('recomend.html' , hasil_pred=hasil, login=login,lokasi = lokasi)
    id = request.args['idr']
    id = int(id)
    hasil=get_recom_hotel(id)
    login=recom(id)
    return render_template('result_login.html', hasil_pred=hasil, login=login,idr=id,data_location=sorted(location))


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/plots')    
def plots():    
    data=Dist_harga()
    data1=Dist_harga1()
    data2=Dist_harga2()
    data3=Dist_harga3()
    data4=Dist_harga4()
    return render_template('plots.html',data=data,data1=data1,data2=data2,data3=data3,data4=data4)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True,port=3333)