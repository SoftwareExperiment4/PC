from django.conf.urls import patterns, include, url
from post_service.views import post_list

urlpatterns = [
	url(r'^$', post_list),
]
