from django.forms import widgets
from rest_framework import serializers
from presta_viticoles.models import *

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
		model = ActivityPrestaViticole
		depth = 1
class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = ("name","description","siret","description")
class ConfigPrestaViticoleSerializer(serializers.ModelSerializer):
	class Meta:
		model = ConfigPrestaViticole

class GroupActivitiesSerializer(serializers.ModelSerializer):
    groups = ActivitiesSerializer(read_only=True, many=True)
    class Meta:
        model = ActivityGroup
        fields =("name","groups")