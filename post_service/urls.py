from django.conf.urls import patterns, include, url
from post_service.views import post_list, post_write

urlpatterns = [
	url(r'^$', post_list),
	url(r'^write/$', post_write, name='write'),
]
