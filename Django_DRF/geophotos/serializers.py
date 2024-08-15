from rest_framework import serializers
from .models import GeoPhoto

class GeoPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoPhoto
        fields = '__all__'