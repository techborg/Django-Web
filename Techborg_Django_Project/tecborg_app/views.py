from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request,'index.html') 
    
    HttpResponse("home")

def innovation(request):
    return render(request,'innovation.html') 
    
    HttpResponse("innovation")

def conact(request):
    return render(request,'conact.html') 
    
    HttpResponse("conact")

def about(request):
    return render(request,'about.html') 
    
    HttpResponse("about")