from http.client import PAYMENT_REQUIRED
# from tkinter import CASCADE
from turtle import title
from xmlrpc.client import DateTime
from django.db import models

class Librarian(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Password = models.CharField(max_length=50)
    UserName = models.CharField(max_length=100)
    Email =models.CharField(max_length=128)
    

    def __str__(self):
        return self.UserName


class Book(models.Model):
    PostBook = models.ForeignKey(Librarian, on_delete = models.CASCADE)
    author = models.CharField(max_length=100)
    book_title = models.CharField(max_length=200)
    publish_date = models.DateField()
    book_id = models.CharField(max_length=100)
    Status = models.CharField(max_length=1000, default="available")
    book_collection = models.CharField(max_length=300)

    def __str__(self):
        return self.book_title
class Student(models.Model):
    UserName= models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    FirstName= models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Email = models.EmailField(max_length=128)


    def __str__(self):
        return self.username
class Borrowers (models.Model):
    borrowedBook= models.ForeignKey(Book, on_delete=models.CASCADE)
    Return_date=models.DateTimeField()
    Date_taken=models.DateTimeField()
    username= models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Payments(models.Model):
    fine=models.ForeignKey(Student,on_delete=models.CASCADE)
    book_id=models.CharField(max_length=100)
    PAYMENT_REQUIRED=models.CharField(max_length=100)
    DatePaid=models.DateTimeField(auto_now_add=True)
    Date_Bookreturned=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_id
        
    