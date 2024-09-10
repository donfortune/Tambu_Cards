from . import models
from rest_framework import serializers




class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    services = serializers.PrimaryKeyRelatedField(queryset=models.Service.objects.all(), many=True)
    
    class Meta:
        model = models.Card
        fields = '__all__'

