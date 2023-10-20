from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models, serializers
# from rest_framework.decorators import api_view

# Create your views here.

class contentsListAPI(APIView):
    def get(self, request):
        contents = models.Content.objects.all()
        serializer = serializers.ContentSerailizer(contents, Many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ContentsViewSet(viewsets.ModelViewSet):
    queryset = models.Content.objects.all()
    serializer_class = serializers.ContentSerailizer


class ContentsDetailViewSet(viewsets.ModelViewSet):
    queryset = models.ContentsDetail.objects.all()
    serializer_class = serializers.ContentDetailSerailizer


class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = models.File.objects.all()
    serializer_class = serializers.FileSerializer
