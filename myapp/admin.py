from django.contrib import admin
from .models import Librarian, Book, Student, Borrowers, Payments

admin.site.register(Librarian)
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Borrowers)
admin.site.register(Payments)

