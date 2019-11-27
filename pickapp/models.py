from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=300)
    category = models.CharField(max_length=100)
    toxic = models.BooleanField()
    maxGrowth = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50)
    airHumidity = models.CharField(max_length=50)
    light = models.CharField(max_length=50)
    watering = models.IntegerField()
    lightDuration = models.IntegerField()
    soil = models.CharField(max_length=200)
    lifespan = models.FloatField()
    image = models.CharField(max_length=300)
    

    def __init__(self, name, url, category, toxic, maxGrowth, temperature,airHumidity, light, watering,lightDuration, soil ,lifespan,image ):
        super().__init__()
        self.name, self.url, self.category, self.toxic,self.maxGrowth,self.temperature,self.airHumidity,self.light,self.watering,self.soil,self.lifespan,self.image,self.lightDuration  = name, url, category,toxic,maxGrowth,temperature,airHumidity,light,watering,soil,lifespan,image,lightDuration

    def fromObject(self,plant):
        self.name = plant["name"]
        self.url = plant["url"]
        self.category = plant["category"]
        self.toxic = plant["toxic"]
        self.image = plant["image"]
        self.lightDuration = plant["lightDuration"]
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
            "lightDuration": self.lightDuration,
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
            }
        }
        return plant
    