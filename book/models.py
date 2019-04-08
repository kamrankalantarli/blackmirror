from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from django.conf import settings



class Product(models.Model):
    SHIRT_SIZES = (
        ('men', 'men'),
        ('women', 'women'),
        ('shoes', 'shoes'),
    )
    SHIRT_SIZE = (
        ('satilir', 'satilir'),
        ('kiraye', 'kiraye'),
        ('deyisdirilir', 'deyisdirilir'),
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    kitab = models.CharField(max_length=120)
    yazar = models.CharField(max_length=120)
    nov = models.CharField(max_length=120,choices=SHIRT_SIZES)
    slug = models.SlugField(blank=True, unique=True)
    qiymet = models.DecimalField(decimal_places=2 , max_digits=20 , default=0)
    image=models.ImageField()
    satis = models.CharField(max_length=120,choices=SHIRT_SIZE)
    publish= models.DateTimeField(auto_now= True, verbose_name="Tarix")

    def __str__(self):
        return self.kitab

    def get_absolute_url(self):
        return "/products/{slug}/".format(slug=self.slug)

    class Meta:
        ordering = ['-publish', 'id']


class Comment(models.Model):
    book = models.ForeignKey('book.Product', related_name='comments', on_delete=models.CASCADE)
    name = models.TextField(verbose_name="şərh")
    create_data = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.comment




