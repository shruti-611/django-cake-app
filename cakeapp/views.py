
from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect



# def home(request):
#     return HttpResponse("Welcome to shrujit bakers !!!")

# def about(request):
#     return HttpResponse("About page")

# def services(request):
#     return HttpResponse("Services page")

# def contact(request):
#     return HttpResponse("Contact page")    

from .models import*

def home(request):
    sg=cakewale.objects.all()
    return render(request,'home.html',{'sg':sg})

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')