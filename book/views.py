from django.shortcuts import render, get_object_or_404
from book.models import *


# Create your views here.


def get_book(request):
    query = Book.objects.all()
    return render(request, "books/books.html", {"books": query})

def view_book_detail(request, id):
    lang_id = get_object_or_404(Book, id=id)
    return render(request, 'books/book_detail.html', {'lang_key': lang_id})