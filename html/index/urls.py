
from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static

from index import views

urlpatterns = patterns('',
        url(r'^$', views.IndexView.as_view(), name='index'),

        ) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
        
