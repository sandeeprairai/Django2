from django.shortcuts import render,redirect
from .models import *

# Create your views here.

# index File View
def IndexPage(request):
    return render(request,"app/index.html")


#upload Image View
def UploadImage(request):
    if request.method=="POST":
        imagename1=request.POST['imgname']
        pics=request.FILES['image']

        newimg=ImageData.objects.create(imagename=imagename1,
                                        Image=pics)
        return redirect('show')
       
        

# Image fetching View
def ImageFetch(request):
    all_img=ImageData.objects.all()
    return render(request,"app/show.html",{'key1':all_img})

