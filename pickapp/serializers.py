from rest_framework import serializers
from .models import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('id', 'name', 'url', 'poisonous', 'maxGrowth', 'temperature', 'light', 'watering', 'soil', 'airHumidity')

    