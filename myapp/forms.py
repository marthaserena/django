from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
#from myapp.models import Student


class CreatUserForm(UserCreationForm):
	first_name= forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	class Meta:
		model = User
		fields = ['last_name', 'first_name' , 'username', 'email', 'password1', 'password2'] 

