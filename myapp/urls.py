from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.Login, name="login"),
    path('register/', views.register, name="register"),
    path('icon/', views.icon, name="icon"),
    path('borrow/<int:id>/', views.borrow, name="borrow"),
    #path('addBorrower', views.addBorrower, name='addBorrower')
    path('borrow/<int:bookid>/borrow', views.borrow, name="borrow"),
    # path('addBorrower', views.addBorrower, name='addBorrower'),
    
]