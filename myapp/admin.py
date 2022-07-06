from django.contrib import admin
from .models import Librarian

admin.site.register(Librarian)
from .models import Book

# Register your models here.
admin.site.register(Book)
from .models import Student

# Register your models here.
admin.site.register(Student)
from .models import Borrowers

admin.site.register(Borrowers)

