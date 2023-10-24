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

class ReviewBook(models.Model):
    STARS = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****'),

    )
    title_lang = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review_object')
    text_review = models.TextField()
    rate_stars = models.CharField(max_length=100, choices=STARS)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
       return f"Review for {self.title_lang}"