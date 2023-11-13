from django.db import models

import CustomerCL.models
import ProductCL.models
from ProductCL import *
from CustomerCL.models import *


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    total = models.IntegerField(verbose_name="Total")
    product = models.ManyToManyField(ProductCL.models.Product)
    date_and_time = models.DateTimeField(auto_now_add=True)
# Create your models here.
