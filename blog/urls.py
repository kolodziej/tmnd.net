from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='blog'),
	url(r'^(?P<category_slug>[0-9a-zA-Z-]+)$', views.category, name='blog_category'),
	url(r'^(?P<post_slug>[0-9a-zA-Z-]+)\.html$', views.read, name='read_post'),
)
