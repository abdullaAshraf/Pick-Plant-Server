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
    Plant("African violet","https://www.houseplantsexpert.com/african-violet-care-information.html","African",False,"40,40","16,24","40,70","1.3,3",3,4,"Loam",2,""),
    Plant("European fan","https://www.houseplantsexpert.com/european-fan-palm.html","European",False,"91,122","4,24","20,30","1.3,3",5,6,"Sandy",10,""),
    Plant("Christmas cheer","https://www.houseplantsexpert.com/christmas-cheer-sedum-rubrotinctum.html","Cheer",True,"30,30","18,24","20,50","0,0.3",20,10,"Sandy",50,"")
]

@api_view(['GET', 'POST'])
def form(request):
    if request.method == 'POST':
        print(request.data)
        data = []
        for plant in plants:
            data.append(plant.toObject())
        return Response(data, status=status.HTTP_201_CREATED)