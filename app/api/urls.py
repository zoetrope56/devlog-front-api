from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'contents', views.ContentsViewSet)
urlpatterns = [
    path('', include(router.urls)),
    # path('contents/', views.contents_list_view),  # 👈 localhost:8000/public
]
