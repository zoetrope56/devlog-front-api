from rest_framework import serializers
from app.api import models

class ContentSerailizer(serializers.ModelSerializer):
    class Meta:
        model = models.Contents
        fields = '__all__'