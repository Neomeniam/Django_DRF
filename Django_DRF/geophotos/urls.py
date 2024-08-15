from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PhotoViewSet

router = DefaultRouter()
router.register(r'geophotos', PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
