# forex/views.py
from django.shortcuts import render
from .models import Card
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CardSerializer

def get_cards_info():
    # Mock data for GreyFinance debit card exchange rate and supported services
    cards_info = [
        {
            'card_name': 'GreyFinance',
            'exchange_rate': '740 NGN/USD',
            'supported_services': ['Udemy', 'Apple Music', 'Spotify', 'Netflix', 'Amazon Prime'],
        },
        {
            'card_name': 'Barter by Flutterwave',
            'exchange_rate': '745 NGN/USD',
            'supported_services': ['Spotify', 'Google Play Store', 'Apple Music', 'Uber', 'Netflix'],
        },
        {
            'card_name': 'ALAT by Wema',
            'exchange_rate': '750 NGN/USD',
            'supported_services': ['Amazon', 'eBay', 'Udemy', 'Google Ads', 'Apple Music'],
        },
        {
            'card_name': 'UBA Dollar Card',
            'exchange_rate': '760 NGN/USD',
            'supported_services': ['PayPal', 'Amazon', 'Google Play Store', 'Netflix', 'Spotify'],
        },
        {
            'card_name': 'GTBank Dollar Card',
            'exchange_rate': '755 NGN/USD',
            'supported_services': ['Apple Music', 'Spotify', 'Netflix', 'Amazon Prime', 'Uber'],
        },
        {
            'card_name': 'Fairmoney Dollar Card',
            'exchange_rate': '755 NGN/USD',
            'supported_services': ['Apple Music', 'Spotify', 'Netflix', 'Amazon Prime', 'Uber'],
        },
        {
            'card_name': 'Vella Dollar Card',
            'exchange_rate': '755 NGN/USD',
            'supported_services': ['Apple Music', 'Spotify', 'Netflix', 'Amazon Prime', 'Uber'],
        },
        {
            'card_name': 'ChipperCash Dollar Card',
            'exchange_rate': '755 NGN/USD',
            'supported_services': ['Apple Music', 'Spotify', 'Netflix', 'Amazon Prime', 'Uber'],
        },
        {
            'card_name': 'EcoBank Dollar Card',
            'exchange_rate': '755 NGN/USD',
            'supported_services': ['Apple Music', 'Spotify', 'Netflix', 'Amazon Prime', 'Uber'],
        },
    ]
    return cards_info

def home(request):
    cards_info = get_cards_info()
    context = {
        'cards_info': cards_info
    }
    return render(request, 'home.html', context)

@api_view(['GET'])
def get_cards(request):
    spec_card = Card.objects.all()
    serializer = CardSerializer(spec_card, many=True)
    return Response(serializer.data)


