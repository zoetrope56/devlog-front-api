from rest_framework import serializers
from app.api import models

class ContentSerailizer(serializers.ModelSerializer):
    class Meta:
        model = models.Contents
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tags
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.File
        fields = '__all__'