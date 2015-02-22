from django.forms import widgets
from rest_framework import serializers
from presta_viticoles.models import *

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
		model = ActivityPrestaViticole
		fields = ("id","description","price_plant_gs","price_plant_gd","price_ha_gs","price_ha_gd","name")
class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = ("name","description","siret","description")
class ConfigPrestaViticoleSerializer(serializers.ModelSerializer):
	class Meta:
		model = ConfigPrestaViticole

class GroupActivitiesSerializer(serializers.ModelSerializer):
    activities = ActivitiesSerializer(many=True,read_only=True)
    class Meta:
        model = ActivityGroup
        fields = ('name', 'activities')