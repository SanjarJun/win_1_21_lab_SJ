from django.urls import path
from book.views import *

urlpatterns = [
    path('', get_book),
    path('lang_detail/<int:id>/', view_book_detail)
]
