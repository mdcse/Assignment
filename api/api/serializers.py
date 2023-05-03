from rest_framework import serializers
from .models import Work, Artist

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    works = WorkSerializer(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = '__all__'
