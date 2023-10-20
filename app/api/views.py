from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models, serializers
from .pagination import Pagination
# from rest_framework.decorators import api_view

# Create your views here.

class ContentsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Content.objects.all()
    serializer_class = serializers.ContentSerailizer
    pagination_class = Pagination 

class ContentsDetailViewSet(viewsets.ModelViewSet):
    queryset = models.ContentsDetail.objects.all()
    serializer_class = serializers.ContentDetailSerailizer
    pagination_class = None


class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    pagination_class = None


class FileViewSet(viewsets.ModelViewSet):
    queryset = models.File.objects.all()
    serializer_class = serializers.FileSerializer
    pagination_class = None
