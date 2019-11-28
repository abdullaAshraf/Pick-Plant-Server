from django.shortcuts import render
from rest_framework import viewsets
from .models import Plant
from .serializers import PlantSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .prediction import predict_plant
import numpy as np
import csv
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import os

class PlantView(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

'''
#def __init__(self, name, category, toxic, maxGrowth, temperature,airHumidity, light, watering, soil ,lifespan,image,match = 0,url = ""):
plants = [
    Plant("African violet","African",False,"40,40","16,24","40,70","1.3,3",3,"Loam",2,"https://www.flowerpower.com.au/media/catalog/product/cache/e4d64343b1bc593f1c5348fe05efa4a6/1/7/172100_1.jpg",.95),
    Plant("European fan","European",False,"91,122","4,24","20,30","1.3,3",5,"Sandy",10,"https://www.jacques-briant.fr/8655-large_default/chamaerops-humilis.jpg",.87),
    Plant("Christmas cheer","Cheer",True,"30,30","18,24","20,50","0,0.3",20,"Sandy",50,"https://i5.walmartimages.com/asr/b7adbabd-d489-45b7-b455-3bd3cfe09075_1.68c054478460f022de918cf9e44c13e7.jpeg",.74)
]
'''
@api_view(['POST'])
def form(request):
    if request.method == 'POST':
        print(request.data)
        names,perceision = pickML(request.data)
        data = getPlants(names,perceision)
        #for plant in plants:
        #    data.append(plant.toObject())
        return Response(data, status=status.HTTP_201_CREATED)

def getPlants(names, perceision):
    plants = []
    plantsList = fillDatabase()
    for plant in plantsList:
        for i,name in enumerate(names):
            if name.strip() == plant["name"]:
                plant["match"] = perceision[i]
                plants.append(plant)
    return plants


def pickML(plant):
    toxic = 0
    if(plant["toxic"]):
        toxic = 1
    MWatering = IWatering = DWatering = 0
    if(plant["watering"] <= 2):
        MWatering = 1
    elif(plant["watering"] <= 20):
        IWatering = 1
    else :
        DWatering = 1
    humidity = (plant["airHumidity"]["min"] + plant["airHumidity"]["max"]) / 2
    light = plant["light"]["min"] * 3.28084
    temp = (plant["temperature"]["min"] * 9/5) + 32
    lifespan = plant["lifespan"]
    diameter = plant["maxGrowth"]["diameter"]
    height = plant["maxGrowth"]["height"]
    Sandy = Clay = Silt = Peat = Chalk = Loam = Soilless = 0
    if(plant["soil"] == "Sandy"):
        Sandy = 1
    elif(plant["soil"] == "Clay"):
        Clay = 1
    elif(plant["soil"] == "Silt"):
        Silt = 1
    elif(plant["soil"] == "Peat"):
        Peat = 1
    elif(plant["soil"] == "Chalk"):
        Chalk = 1
    elif(plant["soil"] == "Loam"):
        Loam = 1
    elif(plant["soil"] == "Soil-less"):
        Soilless = 1

    #toxic,MWatering,IWatering,DWatering,Humidity,Light,Temp,LifeSpan,height,Diameter,Sandy,Clay,Silt,Peat,Chalk,Loam,Soil-less
    in_features = np.array([toxic, MWatering, IWatering, DWatering, humidity, light,temp, lifespan,
                        height, diameter, Sandy, Clay,Silt,Peat,Chalk,Loam,Soilless])
    names,perceision = predict_plant.predict_plant(in_features)
    return names,perceision

def fillDatabase():
    plantsList = list(Plant.objects.all())
    plantsData = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path +'/first_look.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                name = row[0].strip()
                water = 0
                if(row[2] == "M"):
                    water = 1
                elif(row[2] == "I"):
                    water = 3
                else:
                    water = 21

                if(row[3] == 'H'):
                    humidity = {
                        "min": 50,
                        "max": 100,
                    }
                elif(row[3] == 'M'):
                    humidity = {
                        "min": 30,
                        "max": 50,
                    }
                else:
                    humidity = {
                        "min": 20,
                        "max": 30,
                    }

                if(row[4] == 'H'):
                    light = {
                        "min": 0.0,
                        "max": 1.2,
                    }
                elif(row[4] == 'M'):
                    light = {
                        "min": 1.2,
                        "max": 2.4,
                    }
                else:
                    light = {
                        "min": 2.4,
                        "max": 5,
                    }
                
                minTemp = row[5].split('-')[0]
                temp = {
                    "min": int((int(minTemp) - 32) * 5/9),
                    "max": int((int(minTemp) - 32) * 5/9) + 40
                }
                lifespan = float(row[6].split('-')[-1])
                heightList = row[7].split('-')
                heightList = list(map(int, heightList)) 
                diaList = row[8].split('-')
                diaList = list(map(int, diaList)) 
                maxGrowth = {
                    "diameter" : round(sum(diaList) / len(diaList)),
                    "height" : round(sum(heightList) / len(heightList))
                }
                toxic = row[9] == "1"
                soil = []
                if(row[10] == "1"):
                    soil.append("Sandy")
                if(row[11] == "1"):
                    soil.append("Clay")
                if(row[12] == "1"):
                    soil.append("Silt")
                if(row[13] == "1"):
                    soil.append("Peat")
                if(row[14] == "1"):
                    soil.append("Chalk")
                if(row[15] == "1"):
                    soil.append("Loam")
                if(row[16] == "1"):
                    soil.append("Soil-less")
                soilStr = ",".join(soil)
                category = row[17]
                image = row[18]
                #def __init__(self, name, category, toxic, maxGrowth, temperature,airHumidity, light, watering, soil ,lifespan,image,match = 0,url = ""):
                maxGrowthStr = ",".join(str(x) for x in  maxGrowth.values())
                tempStr = ",".join(str(x) for x in  temp.values())
                humidityStr = ",".join(str(x) for x in  humidity.values())
                lightStr = ",".join(str(x) for x in  light.values())
                #plant = Plant(name,category,toxic,maxGrowthStr,tempStr,humidityStr,lightStr,water,soilStr,lifespan,image)
                plant = {
                    "name" : name,
                    "category": category,
                    "toxic" : toxic,
                    "maxGrowth" : maxGrowth,
                    "temperature" : temp,
                    "airHumidity" : humidity,
                    "light" : light,
                    "watering" : water,
                    "soil" : soilStr,
                    "lifespan" : lifespan,
                    "image" : image,
                    "url" : "none",
                    "match" : float(0)
                }
                plantsData.append(plant)
                '''
                serializer = PlantSerializer(data=plant)
                if(serializer.is_valid()):
                    validName = True
                    for plant in plantsList:
                        if(plant.name == name):
                            validName = False
                            break
                    if(validName):
                        serializer.save()
                '''
                #print(serializer.validated_data)
            line_count += 1
            
    return plantsData

#fillDatabase()