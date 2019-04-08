from django.shortcuts import get_object_or_404, render , HttpResponseRedirect
from .models import Product
from .forms import CommentaForm

def index(request):
    queryset = Product.objects.all()
    context = {
        'object_list':queryset
    }
    return render(request,"book/index.html",context)





def detail(request , id):
    #queryset = Product.objects.all()
    instace= get_object_or_404(Product,id=id)
    form = CommentaForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.book = instace
        comment.save()
        return HttpResponseRedirect(instace.get_absolute_url())
    context = {
        'form':form,
        'object': instace,
    }
    return render(request,"book/detail.html",context)