"""
URL configuration for Django_DRF project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf.urls import url, include
#from django.urls import include, re_path
from django.urls import include, path
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from musics import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views  


router = DefaultRouter()
router.register('musics', views.MusicsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/users/', include('users.urls')),
    path('api/musics', include('musics.urls')),
    path('api/geophotos', include('geophotos.urls')),
    path('api/geophotos_with_membership/', include('geophotos_with_membership.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)