from django.urls import path
from OrderCL.views import *

urlpatterns = [
    path("", create_order_class.as_view(), name="create_order")
]
