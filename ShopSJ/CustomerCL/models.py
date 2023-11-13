from django.db import models


class Customer(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255)
    address = models.CharField(verbose_name="Address", max_length=255)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# Create your models here.
