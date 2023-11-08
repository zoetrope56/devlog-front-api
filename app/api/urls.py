from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# router.register(r'contents', ContentsView.as_view())
router.register(r'content', views.ContentsDetailViewSet)
router.register(r'ctags', views.ContentsTagViewSet)
router.register(r'file', views.FileViewSet)
router.register(r'tags', views.TagViewSet)

urlpatterns = [
    path('contents', views.ContentsView.as_view()),
    path('', include(router.urls))
    # path('api/cont', contentsListAPI.as_view())
]
