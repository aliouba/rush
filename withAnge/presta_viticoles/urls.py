from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from presta_viticoles.views import *
from rest_framework import routers


urlpatterns = patterns('',
	url(r'^company/$', CompanyList.as_view()),
)
