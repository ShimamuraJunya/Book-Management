from django.shortcuts import render
from django.utils import timezone
from .models import Book


def book_list(request):
    books=Book.objects.filter(enrolled_date__lte=timezone.now()).order_by('enrolled_date')
    return render(request, 'book/book_list.html', {'books':books})

# Create your views here.
