from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home),
    path('predict/',views.predict),
    path('predict/result',views.result),    
]