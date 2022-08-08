from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.Login, name="login"),
    path('register/', views.register, name="register"),
    path('icon/', views.icon, name="icon"),
    path('borrow/<int:book_id>/borrow', views.borrow, name="borrow")
    
]