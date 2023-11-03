from django.urls import path
from book.views import *

urlpatterns = [
    path('', get_book_class.as_view()),
    path('book_detail/<int:id>/', view_book_detail_class.as_view()),
    path('add-comment/', createBookReview),
    path('book_list/', book_delete_view),
    path('book_list/<int:id>/delete/', book_drop_view_2.as_view()),
    path('create_book/', create_book_class.as_view()),
    path('book_list/<int:id>/update/', update_book_class.as_view()),
    path('search/', SearchView.as_view(), name='search')

]
