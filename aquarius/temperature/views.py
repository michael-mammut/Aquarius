from django.forms import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .models import Temperature
from .serializer import TemperatureSerializer


def current_temperature(request):
    t = Temperature(position="TOP", name="oberer Sensor")
    t.minimum = -1
    t.maximum = -1
    t.current = -1
    t.save()
    s = TemperatureSerializer(t)
    return JsonResponse(model_to_dict(t))
