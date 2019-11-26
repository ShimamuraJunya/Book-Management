from django.contrib import admin
from .models import General_employee
from .models import Book
from .models import Book_record
from .models import Reservation
from .models import Review

admin.site.register(General_employee)
admin.site.register(Book)
admin.site.register(Book_record)
admin.site.register(Reservation)
admin.site.register(Review)
# Register your models here.
