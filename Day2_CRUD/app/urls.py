from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.InsertpageView,name="insertpage"),
    path("insert/",views.InsertData,name="insert"),
    
]