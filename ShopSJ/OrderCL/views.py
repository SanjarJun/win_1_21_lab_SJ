from django.shortcuts import render
from django.views import generic

from OrderCL import forms
from OrderCL.models import *



class create_order_class(generic.CreateView):
    template_name = "create_order.html"
    form_class = forms.OrderForm
    queryset = Order.objects.all()
    success_url = "/"


# Create your views here.
