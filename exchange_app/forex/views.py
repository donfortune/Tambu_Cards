# forex/views.py
from django.shortcuts import render
from .models import Card, Service
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CardSerializer, ServiceSerializer
from rest_framework import status
import requests


def home(request):
    cards_info = Card.objects.all()
    context = {
        'cards_info': cards_info,
    }
    return render(request, 'home.html', context)

def services(request):
    services = Service.objects.all()
    context = {
        'services': services
    }
    return render(request, 'services.html', context)

@api_view(['GET'])
def get_cards(request):
    spec_card = Card.objects.all()
    serializer = CardSerializer(spec_card, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_cards(request):
    data = request.data
    serializer = CardSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_services(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_services(request):
    data = request.data
    serializer = ServiceSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)