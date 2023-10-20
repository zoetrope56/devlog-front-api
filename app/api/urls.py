from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ContentsView, ContentsDetailViewSet, ContentsTagViewSet, FileViewSet, TagViewSet

router = DefaultRouter()

# router.register(r'contents', ContentsView.as_view())
router.register(r'content', ContentsDetailViewSet)
router.register(r'ctags', ContentsTagViewSet)
router.register(r'file', FileViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('contents', ContentsView.as_view()),
    path('', include(router.urls))
    # path('api/cont', contentsListAPI.as_view())
]
