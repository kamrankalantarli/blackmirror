from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Product
from  .forms import CommentaForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
def cart_home(request):
    queryset = Product.objects.all()
    query = request.GET.get('q')


    paginator = Paginator(queryset, 20)  # Show 5 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    context = {
        'object_list': posts
    }
    return render(request,'book/index.html', context)
def post_detail(request , id):
    instace= get_object_or_404(Product,id=id)
    form = CommentaForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.book = instace
        comment.save()
    context = {
        'form':form,
        'object': instace,
    }
    return render(request,"book/detail.html",context)
