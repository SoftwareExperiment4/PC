from django.conf.urls import patterns, include, url
from post_service.views import post_list, login, login_validate

urlpatterns = [
	url(r'^$', post_list),
]