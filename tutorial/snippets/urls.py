from django.conf.urls import url
from django.conf.urls import patterns, include, url
from django.contrib import admin
from snippets import views
urlpatterns = [
	url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]