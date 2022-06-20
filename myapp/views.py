from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "myapp/userpage.html")

def login(request):
    return render(request, "myapp/login.html")

def register(request):
    return render(request, "myapp/register.html")
