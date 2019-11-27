from django.shortcuts import render
from rest_framework import viewsets
from .models import Plant
from .serializers import PlantSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

class PlantView(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

plants = [
    Plant("African violet","https://www.houseplantsexpert.com/african-violet-care-information.html","African",False,"40,40","16,24","40,70","1.3,3",3,4,"Loam",2,"https://www.flowerpower.com.au/media/catalog/product/cache/e4d64343b1bc593f1c5348fe05efa4a6/1/7/172100_1.jpg",.95,1),
    Plant("European fan","https://www.houseplantsexpert.com/european-fan-palm.html","European",False,"91,122","4,24","20,30","1.3,3",5,6,"Sandy",10,"https://www.jacques-briant.fr/8655-large_default/chamaerops-humilis.jpg",.87,2),
    Plant("Christmas cheer","https://www.houseplantsexpert.com/christmas-cheer-sedum-rubrotinctum.html","Cheer",True,"30,30","18,24","20,50","0,0.3",20,10,"Sandy",50,"https://i5.walmartimages.com/asr/b7adbabd-d489-45b7-b455-3bd3cfe09075_1.68c054478460f022de918cf9e44c13e7.jpeg",.74,3)
]

@api_view(['GET', 'POST'])
def form(request):
    if request.method == 'POST':
        print(request.data)
        data = []
        for plant in plants:
            data.append(plant.toObject())
        return Response(data, status=status.HTTP_201_CREATED)