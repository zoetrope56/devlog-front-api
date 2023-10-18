from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models, serializers
# from rest_framework.decorators import api_view

# Create your views here.
class ContentsViewSet(viewsets.ModelViewSet):
    queryset = models.Contents.objects.all()
    serializer_class = serializers.ContentSerailizer
        # return Response(serializer.data)

# contents_list_view = ContentsViewSet.as_view()