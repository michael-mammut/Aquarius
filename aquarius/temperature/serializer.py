from rest_framework import serializers
from .models import Temperature


# set each field to run the example of JSONParser in https://www.django-rest-framework.org/tutorial/1-serialization/
# successful
class TemperatureSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    position = serializers.CharField(max_length=64, required=True)
    name = serializers.CharField(max_length=64, required=True)
    current = serializers.IntegerField(default=-1)
    maximum = serializers.IntegerField(required=True)
    minimum = serializers.IntegerField(default=-1)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Temperature.object.create(**validated_data)

    def update(self, instance, validated_data):
        """
             Update and return an existing `Snippet` instance, given the validated data.
             """
        instance.position = validated_data.get('position', instance.position)
        instance.name = validated_data.get('name', instance.name)
        instance.current = validated_data.get('current', instance.current)
        instance.maximum = validated_data.get('maximum', instance.maximum)
        instance.minimum = validated_data.get('minimum', instance.minimum)
        instance.save()
        return instance
