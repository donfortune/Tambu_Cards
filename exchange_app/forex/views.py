# forex/views.py
from django.shortcuts import render
from .models import Card, Service
from forex.models import Offers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CardSerializer, ServiceSerializer, OffersSerializer
from rest_framework import status
import requests


def home(request):
    cards_info = Card.objects.all()
    offers = Offers.objects.all()
    context = {
        'cards_info': cards_info,
        'offers': offers
    }
    return render(request, 'home.html', context)

def services(request):
    services = Service.objects.all()
    print(services)
    context = {
        'services': services
    }
    return render(request, 'services.html', context)


# def offers(request):
#     offers = Offers.objects.all()
#     print(offers)
#     context = {
#         'offers': offers
#     }
#     return render(request, 'home.html', context)

def offers(request):
    offers = Offers.objects.all()
    for offer in offers:
        print(offer.name, offer.description)
    context = {
        'offers': offers
    }
    return render(request, 'home.html', context)


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

@api_view(['GET'])
def get_offers(request):
    offers = Offers.objects.all()
    serializer = OffersSerializer(offers, many=True)
    return Response(serializer.data)


// add functionality to compare cards and rates
