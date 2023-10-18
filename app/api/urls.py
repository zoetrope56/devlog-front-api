from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ContentsViewSet, FileViewSet, TagViewSet

router = DefaultRouter()

router.register(r'contents', ContentsViewSet)
router.register(r'file', FileViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls))
]
