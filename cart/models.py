from django.db import models
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
    publish = models.DateTimeField(auto_now= True, verbose_name="Tarix")

    def __str__(self):
        return self.kitab


    class Meta:
        ordering = ['-publish', 'id']


class Comment(models.Model):
    book = models.ForeignKey('cart.Product', related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=120, verbose_name="adiniz")
    sname = models.CharField(max_length=120 ,verbose_name="soyadiniz")
    email=models.EmailField(verbose_name="email")
    g = models.DateField(verbose_name="gorush")
    s = models.TimeField(verbose_name="saat")
    d = models.BooleanField(verbose_name="Sertleri qebul edirem")
    create_data = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-create_data', 'id']