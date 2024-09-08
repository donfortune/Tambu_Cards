from . import models
from rest_framework import serializers




class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)
    class Meta:
        model = models.Card
        fields = '__all__'