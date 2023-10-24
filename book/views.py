from django.shortcuts import render, get_object_or_404
from book import forms
from book.models import *
from django.http import HttpResponse

# Create your views here.


def get_book(request):
    query = Book.objects.all()
    return render(request, "books/books.html", {"books": query})

def view_book_detail(request, id):
    lang_id = get_object_or_404(Book, id=id)
    return render(request, 'books/book_detail.html', {'lang_key': lang_id})



def create_book (request):
    method = request.method
    if method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Added')
    else:
        form = forms.BookForm()
    return render(request, 'books/create_book.html', {'form': form})

def book_delete_view (request):
    lang_value = Book.objects.all()
    return render(request, 'books/book_list.html', {'lang_key': lang_value})

def book_drop_view (request, id):
    lang_id = get_object_or_404(Book, id=id)
    lang_id.delete()
    return HttpResponse('Deleted')


def createBookReview(request):
    method = request.method
    if method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Comment added</h1>')

    else:
        form = forms.ReviewForm()

    return render(request, 'books/create_review.html', {'form': form})