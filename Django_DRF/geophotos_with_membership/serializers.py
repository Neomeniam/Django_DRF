from rest_framework import serializers
from .models import GeoPhoto

class GeoPhotoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = GeoPhoto
        fields = ['id', 'image', 'latitude', 'longitude', 'comment', 'owner', 'created_at']
        read_only_fields = ['owner']