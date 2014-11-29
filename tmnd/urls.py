from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tmnd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

		url(r'^$', views.index),
    url(r'^admin/', include(admin.site.urls)),
		url(r'^blog/', include('blog.urls')),
)

admin.AdminSite.site_header = 'TMND administration'
