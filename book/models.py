from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(verbose_name='Book Name', max_length=255)
    description = models.TextField(verbose_name='Book Description')
    image = models.ImageField(verbose_name='Image', upload_to='')
    cost = models.IntegerField(verbose_name='Book Price $')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
