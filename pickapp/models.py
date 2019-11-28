from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=300)
    category = models.CharField(max_length=100)
    maxGrowth = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50)
    airHumidity = models.CharField(max_length=50)
    soil = models.CharField(max_length=200)
    light = models.CharField(max_length=50)
    image = models.CharField(max_length=500)
    toxic = models.BooleanField()
    watering = models.IntegerField()
    lifespan = models.FloatField()
    match = models.FloatField()
    
    def fromObject(self,plant):
        self.name = plant["name"]
        self.url = plant["url"]
        self.category = plant["category"]
        self.toxic = plant["toxic"]
        self.image = plant["image"]
        self.soil = plant["soil"]
        self.watering = plant["watering"]
        self.lifespan = plant["lifespan"]
        self.maxGrowth = ",".join(plant["maxGrowth"].values())
        self.temperature = ",".join(plant["temperature"].values())
        self.airHumidity = ",".join(plant["airHumidity"].values())
        self.light = ",".join(plant["light"].values())

    def toObject(self):
        growth = self.maxGrowth.split(',')
        temp = self.temperature.split(',')
        air = self.airHumidity.split(',')
        light = self.light.split(',')
        plant = {
            "name": self.name,
            "url": self.url,
            "category": self.category,
            "soil": self.soil,
            "watering": self.watering,
            "image": self.image,
            "lifespan": self.lifespan,
            "toxic": self.toxic,
            "maxGrowth" : {
                "diameter": int(growth[0]),
                "height": int(growth[1])
            },
            "temperature": {
                "min": int(temp[0]),
                "max": int(temp[1])
            },
            "airHumidity": {
                "min": int(air[0]),
                "max": int(air[1])
            },
            "light": {
                "min": float(light[0]),
                "max": float(light[1])
            },
            "match": self.match,
        }
        return plant