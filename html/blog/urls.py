
from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static

from blog import views

urlpatterns = [
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^post/(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name='detail'),
        url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
#        url(r'^tag/(?P<slug>[-\w]+)/$', views.TaggedIndexView.as_view(), name='tagged'),
        url(r'^page/(?P<slug>[-\w]+)$', views.PageIndexView.as_view(), name='page'),
        url(r'^page/(?P<slug>[-\w]+)/(?P<pk>\d+)/$', views.PageDetail.as_view(), name='page_detail'),
        url(r'^pages/', include('django.contrib.flatpages.urls')),

        ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
       
