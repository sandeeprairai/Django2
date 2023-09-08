from django.shortcuts import render

# Create your views here.
def IndexView(request):  #Index.html View
    return render(request,"app/index.html")


def htmlform(request):
    return render(request,"app/forms.html")



