from django.contrib.auth.models import User
from rest_framework import serializers
from presta_viticoles.models import *


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
class ConfigPrestaViticoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConfigPrestaViticole
