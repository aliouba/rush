from django.contrib.auth.models import User, Group
from rest_framework import serializers
from snippets.models import *


class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('artist', 'tracks')