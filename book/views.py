from django.shortcuts import render

from book.models import *


# Create your views here.


def get_book(request):
    query = Book.objects.all()
    return render(request, "books/books.html", {"render_book": query})