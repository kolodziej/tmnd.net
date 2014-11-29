from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='blog'),
	url(r'^(?P<page>[0-9]{1,11})$', views.index, name='blog_page'),
	url(r'^(?P<category_slug>[0-9a-zA-Z-]+)$', views.category, name='blog_category'),
	url(r'^(?P<category_slug>[0-9a-zA-Z-]+),(?P<page>[0-9]{1,11})$', views.category, name='blog_category_page'),
	url(r'^(?P<post_slug>[0-9a-zA-Z-]+)\.html$', views.read, name='read_post'),
)
