from django.db import models


#Database'de tabloları oluşturmak için iha modelini belirtiyoruz.

class Iha(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    description = models.TextField()
    maxWeight = models.CharField(max_length=10)
    flightTime = models.CharField(max_length=3)
    altitude = models.CharField(max_length=10)
    armed = models.BooleanField()
    image = models.CharField(max_length=500)
    owner = models.CharField(max_length=100)

