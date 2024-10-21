from django.urls import path
from .views import GeoPhotoListView, GeoPhotoDetailView

urlpatterns = [
    path('geophotos/', GeoPhotoListView.as_view(), name='geophoto-list'),
    path('geophotos/<int:pk>/', GeoPhotoDetailView.as_view(), name='geophoto-detail'),
]