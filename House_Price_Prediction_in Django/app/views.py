from django.shortcuts import render
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Create your views here.
def home(request):
    return render(request,"app/home.html")

def predict(request):
    return render(request,"app/predict.html")

def result(request):
    df=pd.read_csv("C:/Users/sandeepkumar/OneDrive/Desktop/Django/House_Price_Prediction_in Django/app/USA_Housing.csv")
    df=df.drop(['Address'],axis=1)
    X=df.drop('Price',axis=1)
    Y=df['Price']

    #Train-test Split
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.30)

    model=LinearRegression()
    model.fit(X_train,Y_train)
    var1=float(request.GET['n1'])
    var2=float(request.GET['n2'])
    var3=float(request.GET['n3'])
    var4=float(request.GET['n4'])
    var5=float(request.GET['n5'])

    pred=model.predict(np.array([var1,var2,var3,var4,var5]).reshape(1,-1))
    pred=round(pred[0])

    price="The Predicted price is $"+str(pred)


    


    return render(request,"app/predict.html",{"result2":price})



