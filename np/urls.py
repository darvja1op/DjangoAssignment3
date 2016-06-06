from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.article_list, name='article_list'),
    url(r'^np/new/$', views.article_new, name='article_new'),
	url(r'^np/(?P<pk>\d+)/edit/$', views.article_edit, name='article_edit'),
	url(r'^np/(?P<pk>\d+)/remove/$', views.article_remove, name='article_remove'),
	url(r'^np/(?P<pk>\d+)/$', views.article_detail, name='article_detail'),
	]