from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get-cards/', views.get_cards, name='get_cards'),
    path('create-cards/', views.create_cards, name='create_cards'),
]
