from rest_framework import viewsets, permissions, generics, status
from . import models, serializers
from .pagination import Pagination
from django.db.models import Count

# Create your views here.

class ContentsView(generics.ListAPIView):
    queryset = models.Content.objects.all().order_by('-inp_dttm')
    serializer_class = serializers.ContentSerailizer
    pagination_class = Pagination 

class ContentsDetailViewSet(viewsets.ModelViewSet):
    queryset = models.ContentsDetail.objects.all()
    serializer_class = serializers.ContentDetailSerailizer
    pagination_class = None

class ContentsTagViewSet(viewsets.ModelViewSet):
    queryset = models.ContentsTag.objects.all()
    serializer_class = serializers.ContentsTagSerializer
    pagination_class = None

class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.annotate(tag_count=Count('tags_set')).values('tag_no','tag_name', 'tag_count').order_by('tag_no')
    serializer_class = serializers.TagSerializer
    pagination_class = None


class FileViewSet(viewsets.ModelViewSet):
    queryset = models.File.objects.all()
    serializer_class = serializers.FileSerializer
    pagination_class = None
