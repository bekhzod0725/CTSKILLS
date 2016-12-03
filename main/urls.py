from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from . import views, ajax

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^getdata/$', ajax.getdata, name='getdata'),
        url(r'^getpercapita/$', ajax.get_percapita, name='getpercapita'),
        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
