from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    poisonous = models.CharField(max_length=100)
    maxGrowth = models.CharField(max_length=200)
    temperature = models.CharField(max_length=50)
    light = models.CharField(max_length=50)
    watering = models.FloatField(max_length=100)
    soil = models.CharField(max_length=200)
    airHumidity = models.CharField(max_length=50)

    def __init__(self, name, url, poisonous, maxGrowth, temperature, light, watering, soil , airHumidity):
        self.name, self.url, self.poisonous,self.maxGrowth,self.temperature,self.light,self.watering,self.soil,self.airHumidity  = name, url, poisonous,maxGrowth,temperature,light,watering,soil,airHumidity

    def fromObject(self,plant):
        self.name = plant["name"]
        self.url = plant["url"]
        self.light = plant["light"]
        self.soil = plant["soil"]
        self.watering = plant["watering"]
        self.poisonous = ",".join(plant["poisonous"].keys())
        self.maxGrowth = ",".join(plant["maxGrowth"].values())
        self.temperature = ",".join(plant["temperature"].values())
        self.airHumidity = ",".join(plant["airHumidity"].values())

    def toObject(self):
        growth = self.maxGrowth.split(',')
        temp = self.temperature.split(',')
        air = self.airHumidity.split(',')
        plant = {
            "name": self.name,
            "url": self.url,
            "light": self.light,
            "soil": self.soil,
            "watering": self.watering,
            "poisonous" : {
                "cat": "cat" in self.poisonous,
                "dog": "dog" in self.poisonous
            },
            "maxGrowth" : {
                "width": float(growth[0]),
                "length": float(growth[1]),
                "height": float(growth[2])
            },
            "temperature": {
                "min": float(temp[0]),
                "max": float(temp[1])
            },
            "airHumidity": {
                "min": float(air[0]),
                "max": float(air[1])
            }
        }
        return plant
    