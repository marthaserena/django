from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreatUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Book




def register(request):
	form = CreatUserForm()
	if request.method == "POST":
		form = CreatUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, "Account created for" + user )
			return redirect('login')


	return render(request, "myapp/register.html", {'form': form})




def Login(request):

		if request.method == "POST":
			username = request.POST.get('username')
			password = request.POST.get('password')
			last_name = request.POST.get('last_name')
			first_name = request.POST.get('first_name')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('icon')

			else:
				messages.info(request, 'UserName or Password incorrect')


		return render(request, "myapp/login.html")


def home(request):
	return render(request, "myapp/userpage.html")


def icon(request):
	books = Book.objects.all()
	if request.method =='GET':
		q = request.GET.get('q')
		r = request.GET.get('r')
		t = request.GET.get('t')
		if q:
			books = Book.objects.filter(book_title__icontains=q)
		if r:
			books = Book.objects.filter(book_collection__icontains=r)
		if t:
			books = Book.objects.filter(author__icontains=t)
			
	else:
		books = Book.objects.all()

	return render(request, "myapp/icon.html",{'books':books})


def logout(request):
	logout()
	return redirect('login')


def borrow(request):
	return render(request, "myapp/borrow.html")



