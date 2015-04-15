from django.forms import widgets
from rest_framework import serializers
from presta_viticoles.models import *

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
		model = ActivityPrestaViticole
class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = ("name","description","siret","description")
class ConfigPrestaViticoleSerializer(serializers.ModelSerializer):
	class Meta:
		model = ConfigPrestaViticole

class GroupActivitiesSerializer(serializers.ModelSerializer):
    activities = ActivitiesSerializer(read_only=True, many=True)
    class Meta:
        model = ActivityGroup

class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
class EstimateSerializer(serializers.ModelSerializer):
    estimates = BenefitSerializer(read_only=True,many=True)
    class Meta:
        model = Estimate
class CEstimateSerializer(serializers.Serializer):
    nb = serializers.FloatField()
    price_with_tax = serializers.DecimalField(max_digits=10, decimal_places=3)
    price_without_tax = serializers.DecimalField(max_digits=10, decimal_places=0)
    Benefits = serializers.ListField(
        child = serializers.DecimalField(max_digits=10, decimal_places=3)
        )