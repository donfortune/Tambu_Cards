from django.db import models


SERVICE_CHOICES = [
    ('udemy', 'Udemy'),
    ('apple_music', 'Apple Music'),
    ('spotify', 'Spotify'),
    ('netflix', 'Netflix'),
    ('amazon_prime', 'Amazon Prime'),
    ('google_play', 'Google Play Store'),
    ('uber', 'Uber'),
    ('paypal', 'PayPal'),
    ('ebay', 'eBay'),
    ('google_ads', 'Google Ads'),
]


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )

    card_name = models.CharField(max_length=100)
    exchange_rate = models.FloatField()
    services = models.ManyToManyField(Service)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='active')
    

    def __str__(self):
        return f"{self.card_name} - {self.get_status_display()}"


