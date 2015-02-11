from django.contrib.auth.models import User, Group
from rest_framework import serializers
from snippets.models import *


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('order', 'title','album_id')

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(source='album_id',many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'artist', 'tracks')