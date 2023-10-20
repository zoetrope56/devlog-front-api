from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ContentsViewSet, ContentsDetailViewSet, FileViewSet, TagViewSet, contentsListAPI

router = DefaultRouter()

router.register(r'contents', ContentsViewSet)
router.register(r'content', ContentsDetailViewSet)
router.register(r'file', FileViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/cont', contentsListAPI.as_view())
]
