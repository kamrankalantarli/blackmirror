from django.contrib import admin
from django.conf.urls import url, include

from django.conf.urls.static import static
from django.conf import settings
from home.views import homel
from about.views import aboutl
from contact.views import contactl


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', homel, name='home'),
    url(r'^contact/$', contactl, name='contact'),
    url(r'^about/$', aboutl, name='about'),
    url(r'^products/', include('cart.urls')),
    url('accounts/', include('account.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
