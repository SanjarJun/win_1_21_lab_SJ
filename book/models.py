from django.db import models

# Create your models here.


class Book(models.Model):
    ACTUALITY = (('Actual', 'Actual'), ('50 on 50', '50 on 50'), ('0 on 0','0 on 0'))
    title = models.CharField(verbose_name='Book Name', max_length=255)
    description = models.TextField(verbose_name='Book Description')
    image = models.ImageField(verbose_name='Image', upload_to='')
    actuality = models.CharField(max_length=100, choices=ACTUALITY, default=ACTUALITY[0], null=True)
    video =models.URLField(null=True)
    cost = models.IntegerField(verbose_name='Book Price $')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
