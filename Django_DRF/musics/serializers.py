from rest_framework import serializers
from musics.models import Music


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'
        fields = ('id', 'song', 'singer', 'last_modify_date', 'created', 'owner')

    owner = serializers.ReadOnlyField(source='owner.username')
