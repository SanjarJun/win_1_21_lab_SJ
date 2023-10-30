from django.shortcuts import render, get_object_or_404

from book import forms
from book.models import *
from django.http import HttpResponse
from django.views import generic
# Create your views here.


class get_book_class(generic.ListView):
    template_name = "books/books.html"
    queryset = Book.objects.all()

    def get_queryset(self):
        return Book.objects.all()

# def get_book(request):
#     query = Book.objects.all()
#     return render(request, "books/books.html", {"books": query})

class view_book_detail_class(generic.DetailView):
    template_name = "books/book_detail.html"

    def get_object(self, **kwargs):
        boo = self.kwargs.get("id")
        return get_object_or_404(Book, id=boo)

# def view_book_detail(request, id):
#     lang_id = get_object_or_404(Book, id=id)
#     return render(request, 'books/book_detail.html', {'lang_key': lang_id})


class create_book_class(generic.CreateView):
    template_name = "books/create_book.html"
    form_class = forms.BookForm
    queryset = Book.objects.all()
    success_url = "/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(create_book_class,self).form_valid(form=form)



# def create_book (request):
#     method = request.method
#     if method == "POST":
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<a href="/">Back</a>')
#     else:
#         form = forms.BookForm()
#     return render(request, 'books/create_book.html', {'form': form})

def book_delete_view (request):
    lang_value = Book.objects.all()
    return render(request, 'books/book_list.html', {'lang_key': lang_value})

class book_drop_view_2 (generic.DeleteView):
    template_name = "confirm_delete.html"
    success_url = "/"
    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)

# def book_drop_view (request, id):
#     lang_id = get_object_or_404(Book, id=id)
#     lang_id.delete()
#     return HttpResponse('Deleted')

class update_book_class(generic.UpdateView):
    template_name = "update_book.html"
    form_class = forms.BookForm
    success_url = "/"

    def get_object(self, **kwargs):
        boo = self.kwargs.get("id")
        return get_object_or_404(Book, id=boo)

    def form_valid(self, form):
        return super(update_book_class,self).form_valid(form=form)

class SearchView(generic.ListView):
    template_name='books'
    context_object_name = "book"
    paginate_by = 4

    def get_queryset(self):
        return Book.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context

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