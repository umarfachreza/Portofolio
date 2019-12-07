# Airbnb Amsterdam Price Prediction and Recommendation System

The source of the dataset is from ["Airbnb Amsterdam"](https://www.kaggle.com/erikbruin/airbnb-amsterdam) provided by Kaggle.

## Price Predict using Regression Model
### 1. Data Preprocessing

I use Dataset listing_details.csv. The listings_details file contains a total of 96 coloumns, i am not going to use all of these. In cleaning data I drop coloumns where has missing value more than 40%, has unique value 0, 1 and contains sentences. this dataset has many coloumns about Locations, i choose neighbourhood_cleansed cause the coloumns classification area correctly. 

![price with Neighbourhood](/AIRBNB%20AMSTERDAM/Images/neighbourhood.PNG)

I fill The missing Value with **Groupby** and change dtype the price from object to int. I drop the Outlier Price, and i Clean the Rooms, Bathrooms, bed, accomodation from decimals Value. From Amenities i clean the value from missing, and with **countVectorizer** i create a dataset contains Fasilitas. the last i choose the coloumns with **Corr** Value more then 0.05 or less then -0.05.

### 2. Data Visualization

in data Visualization i display the corr, and the price comparison with each coloumns.

![price with Neighbourhood](/AIRBNB%20AMSTERDAM/Images/Boxplot_Price_neighbourhood.PNG)
Ex: Comparison price with Neighbourhood


### 3. Modelling

Before starting to predict, I compare 5 model machine learning: Linier Regression, Lasso, Ridge, Random Forest Regressor, Gradient Boosting Regressor, and XGBRegressor to find the best model for prediction.

![compare model](/AIRBNB%20AMSTERDAM/Images/Comparison_regresion_model.PNG)

Since **Gradient Boosting Regressor**, and **XGBRegressor** gives the best score among the others, this prediction will use **Gradient Boosting Regressor** for the Price prediction. then i compare modeling with or without **Standard Scaler** and **PCA**, and i get the best modeling is without them. Next i find the best parameter to use with **GridsearchCV** and use that in this model.

![gridsearchCV](/AIRBNB%20AMSTERDAM/Images/Gridsearch.PNG)

From the best parameter we get better MAE From this model.

## Recommendation System

From the last hotel we stay this model find 10 hotel which has similiar fasilitas in your next location and recommended that to you. 

![result recomendation](/AIRBNB%20AMSTERDAM/Images/Recommendation_jp.PNG)

The recommendation system using **cosine_similarity**.

## Dashboard

Using **Flask** and **HTML**, The Price Predict and Recommendation System system would be presented as below:

![Home_page](/AIRBNB%20AMSTERDAM/Images/Home_page.PNG)

### 1. Price Prediction

Before predicting, you should input on the features form before hitting the prediction button as shown below:

![Predict_page](/AIRBNB%20AMSTERDAM/Images/Predict_page.PNG)

The system will give the result of price based on the selected features, the top 5 most expensive places and Price histogram at the selected location. 

![Result_page](/AIRBNB%20AMSTERDAM/Images/Result_page.PNG)

### 2. Recommendation System

The system will give recommendation in location we want based last hotel we stay. first we must login to know data users.

![Login_page](/AIRBNB%20AMSTERDAM/Images/Login_page.PNG)

After Login we can see where we stay on the last trip, and our reviews. in this page we can input our next destination. 

![Result_login_page](/AIRBNB%20AMSTERDAM/Images/Result_login_page.PNG)

After you fill the location, and click on get recomendation. it will bring you to the Recomendation result page. you can see top 10 places to stay in location you choose which has similiar fasilitas with your last hotel.

![Result_recomendation_page](/AIRBNB%20AMSTERDAM/Images/Result_recomendation_page.PNG)


## Thank you for your attention. I hope you enjoy my project. 😊
✉ fachrezaumar@gmail.com
