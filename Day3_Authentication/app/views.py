from django.shortcuts import render
from .models import *

# Create your views here.

#view for register Page

def RegisterPage(request):
    return render(request,"app/register.html")



#View for User register

def UserRegister(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        contact=request.POST['contact']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        #First we will validate that user laready exist
        user1=user.objects.filter(Email=email)

        if user1:
            message="User already exist"
            return render(request,"app/register.html",{'msg':message})
        
        else:
            if password==cpassword:
                newuser=user.objects.create(Firstname=fname,
                                            Lastname=lname,
                                            Email=email,
                                           Contact=contact,Password=password)
                message="user register Succesfully"
                return render(request,"app/login.html",{'msg':message})
            else:
                message="Password  and Confirm Password Doesn't Match"
                return render(request,"app/register.html",{'msg':message})
            
        

 #Login view           
def LoginPage(request):
    return render(request,"app/login.html")

#Login User
def LoginUser(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']

        # Checking email-id with database
        user2=user.objects.get(Email=email)

        if user2:
            if user2.Password==password:
                # We are gettinguser data in session
                request.session['Firstname']=user2.Firstname
                request.session['Lastname']=user2.Lastname
                request.session['Email']==user2.Email
                return render(request,"app/home.html")

            else:
                message="Password doesn't match"
                return render(request,"app/login.html",{'msg':message})
            



    else:
        message="User does not exist"
        return render(request,"app/register.html",{'msg':message})
        






