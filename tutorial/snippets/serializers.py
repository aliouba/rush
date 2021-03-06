from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES



from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
