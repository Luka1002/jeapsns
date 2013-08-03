from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from jeapsns.views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jeapsns.views.home', name='home'),
    # url(r'^jeapsns/', include('jeapsns.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
    url(r'^time/get/(.)$',current_time),
    url(r'^system/(.)$',system_info),
    url(r'^index/(.{1,9})$',index_temp),
    url(r'^index_file/(\d{0,9})$',index_temp_file),
    url(r'^delete/$',delete),
    (r'^accounts/register/$', 'jeapsns.views.register'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'})
)
