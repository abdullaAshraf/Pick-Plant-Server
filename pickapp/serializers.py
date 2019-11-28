from rest_framework import serializers
from .models import Plant

class PlantSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    url = serializers.CharField(max_length=300)
    category = serializers.CharField(max_length=100)
    toxic = serializers.BooleanField()
    maxGrowth = serializers.CharField(max_length=50)
    temperature = serializers.CharField(max_length=50)
    airHumidity = serializers.CharField(max_length=50)
    light = serializers.CharField(max_length=50)
    watering = serializers.IntegerField()
    soil = serializers.CharField(max_length=200)
    lifespan = serializers.FloatField()
    image = serializers.CharField(max_length=500)
    match = serializers.FloatField()
    
    def create(self, validated_data):
        return Plant.objects.create(**validated_data)

    