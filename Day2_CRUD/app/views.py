from django.shortcuts import render
from .models import *

# Create your views here.

def InsertpageView(request):
    return render(request,"app/insert.html")

def InsertData(request):
    #data come from HTML to view
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    contact=request.POST['contact']

    #creating Object of Model Class
    #Inserting data into table
    newuser=Student.objects.create( Firstname=fname,
                                   Lastname=lname,
                                   Email=email,
                                   Contact=contact)
    
    #after Insert render on show page
    return render(request,"app/show.html")


