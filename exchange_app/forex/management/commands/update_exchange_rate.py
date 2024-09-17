from django.core.management.base import BaseCommand
from forex.models import Card
import requests
from decouple import config

class Command(BaseCommand):
    help = 'Update exchange rate of all cards'

    def handle(self, *args, **kwargs):
        api_key = config('EXCHANGE_RATE_API_KEY')
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
        response = requests.get(url)
        data = response.json()

        if data['result'] == 'success':
            ngn_rate = data['conversion_rates']['NGN']
            # Update all card objects with the latest exchange rate
            cards = Card.objects.all()
            for card in cards:
                card.exchange_rate = ngn_rate
                card.save()
            self.stdout.write(self.style.SUCCESS(f'Updated exchange rate to {ngn_rate} for all cards'))
        else:
            self.stdout.write(self.style.ERROR('Error fetching exchange rate'))
