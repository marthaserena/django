from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, "myapp/userpage.html")
    

def login(request):
    return render(request, "myapp/login.html")

def register(request):
    if request.method == "POST":
        first_name = request.POST[first_name]
        last_name = request.POST[last_name]
        email = request.POST[email]
        user_name = request.POST[user_name]
        password1 = request.POST[password1]
        password2 = request.POST[password2]

        myuser = User.objects.create_user(email, user_name, password1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()

        messages.success(request, "Your account has been created successfully")

        return redirect("signin")
    return render(request, "myapp/register.html")
    
def icon(request):
    return render(request, "myapp/icon.html")
        
