from django.contrib.auth.models import User, Group
from rest_framework import serializers

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.HyperlinkedRelatedField(
        many=True, view_name='authentication:user-detail', read_only=True)
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'date_joined']
        extra_kwargs = {'url': {'view_name': 'authentication:user-detail'}}