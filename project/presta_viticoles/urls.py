from django.conf.urls import patterns, include, url
from django.contrib import admin
from presta_viticoles.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'nouveauentr', CompanyViewSet)
router.register(r'newconf', ConfigPrestaViticoleViewSet)


urlpatterns = patterns('',
	#url(r'^(?P<company>\d+)/$',ActivitiesView.as_view(),name='activities-list'),
	url(r'^(?P<idCompany>\d+)/$',add_company,name='add company'),
	url(r'^api/',include(router.urls)),
)
