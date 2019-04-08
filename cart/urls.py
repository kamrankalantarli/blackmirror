from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^$', cart_home,name='cart'),
    url(r'^(?P<id>\d+)/detail/$', post_detail),


]