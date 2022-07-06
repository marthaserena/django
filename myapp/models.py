from turtle import title
from django.db import models

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
