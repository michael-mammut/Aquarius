from django.db import models


class Temperature(models.Model):
    position = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    current = models.IntegerField
    maximum = models.IntegerField
    minimum = models.IntegerField
