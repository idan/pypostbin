from django.conf.urls.defaults import *

urlpatterns = patterns('postbin.views',
    url(r'^$', 'create', name='create'),
    url(r'^(?P<id>\d+)/$', 'view', name='view'),
)