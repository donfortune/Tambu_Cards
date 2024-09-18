from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('offers/', views.offers, name='offers'),
    path('get-cards/', views.get_cards, name='get_cards'),
    path('create-cards/', views.create_cards, name='create_cards'),
    path('get-services/', views.get_services, name='get_services'),
    path('create-services/', views.create_services, name='create_services'),
    path('get-offers/', views.get_offers, name='get_offers'),
]
