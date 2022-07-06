from turtle import title
from django.db import models

class Librarian(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Password = models.CharField(max_length=50)
    UserName = models.CharField(max_length=100)

    def __str__(self):
        return self.UserName

# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=100)
    book_title = models.CharField(max_length=200)
    publish_date = models.DateField()
    book_id = models.CharField(max_length=100)
    book_image = models.CharField(max_length=1000)
    book_collection = models.CharField(max_length=300)

    def __str__(self):
        return self.book_title
class Student(models.Model):
    UserName= models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    FirstName= models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Email =models.CharField(max_length=128)


    def __str__(self):
        return self.UserName
class Borrowers (models.Model):
    book_id= models.CharField
    Return_date=models.DateField
    Date_taken=models.DateField
