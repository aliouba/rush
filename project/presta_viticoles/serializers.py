from django.contrib.auth.models import User
from rest_framework import serializers
from presta_viticoles.models import *


class ConfigPrestaViticoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConfigPrestaViticole
class ActivityPrestaViticoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPrestaViticole

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
