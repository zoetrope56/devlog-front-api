from rest_framework import serializers
from app.api import models


class ContentSerailizer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Content
        fields = '__all__'

class ContentDetailTagSerailizer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Content
        fields = ['tags']


class ContentDetailSerailizer(serializers.ModelSerializer):
    ctnt_mst = ContentDetailTagSerailizer()

    class Meta:
        model = models.ContentsDetail
        fields = '__all__'


class ContentsTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContentsTag
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.File
        fields = '__all__'
