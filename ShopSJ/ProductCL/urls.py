from django.urls import path

from ProductCL.views import *

app_name = 'product'

urlpatterns = [
    path("", ProductsView.as_view(), name="products"),
    path("products", ProductFilterView.as_view(), name="tags_filter")
]
