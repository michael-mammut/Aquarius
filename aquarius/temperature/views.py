from typing import Type, Tuple

from django.forms import model_to_dict
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Temperature
from .serializer import TemperatureSerializer


class TemperatureView(APIView):
    permission_classes: Tuple[Type[IsAuthenticated]] = (IsAuthenticated,)

    def get(self, request):
        request.data
        t = Temperature(position="TOP", name="oberer Sensor")
        t.minimum = -1
        t.maximum = -1
        t.current = -1
        t.save()
        s = TemperatureSerializer(t)
        return JsonResponse(model_to_dict(t))
