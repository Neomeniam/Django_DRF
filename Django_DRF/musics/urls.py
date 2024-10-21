from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MusicsViewSet

router = DefaultRouter()
router.register(r'musics', MusicsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]