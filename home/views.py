from django.shortcuts import render
from cart.models import Product
def homel(request):
    bloge = Product.objects.all()
    context = {
        'bloge':bloge
    }
    return render(request,'home/homes.html', context)
