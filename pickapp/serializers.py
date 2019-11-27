from rest_framework import serializers
from .models import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('id', 'name', 'url', 'category','toxic', 'maxGrowth', 'temperature', 'light', 'watering','lightDuration', 'soil','lifespan','image', 'airHumidity')

    