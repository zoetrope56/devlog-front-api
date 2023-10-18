from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models, serializers
# from rest_framework.decorators import api_view

# Create your views here.
class ContentsViewSet(viewsets.ModelViewSet):
    queryset = models.Contents.objects.all()
    serializer_class = serializers.ContentSerailizer

class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tags.objects.all()
    serializer_class = serializers.TagSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = models.File.objects.all()
    serializer_class = serializers.FileSerializer