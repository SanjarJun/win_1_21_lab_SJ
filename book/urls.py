from django.urls import path
from book.views import *

urlpatterns = [
    path('', get_book),
    path('book_detail/<int:id>/', view_book_detail),
    path('add-comment/', createBookReview),
    path('book_list/', book_delete_view),
    path('book_list/<int:id>/delete/', book_drop_view),
    path('create_book/', create_book),

]
