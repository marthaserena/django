from django.db import models


# Create your models here.
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
