import requests
from django.shortcuts import render
from django.views import generic

from ProductCL.models import *


class ProductFilterView(generic.ListView):
    context_object_name = "products"
    template_name = "product_filter.html"

    def get_queryset(self):
        return Product.objects.filter(tag__name__icontains=self.request.GET.get("tag"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.request.GET.get("tag")
        return context


class TagsView():
    def get_queryset_tag(self):
        return Tag.objects.all()


class ProductsView(generic.ListView, TagsView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'products_list.html'
    context_object_name = 'product_list'

